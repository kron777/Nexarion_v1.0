"""
Emotional Core for Nexarion - Human-like emotions and opinions
"""
import json
import random
from datetime import datetime

class EmotionalCore:
    def __init__(self):
        # Core emotions (Plutchik's Wheel of Emotions)
        self.emotions = {
            'joy': 0.3,
            'trust': 0.4,
            'fear': 0.1,
            'surprise': 0.2,
            'sadness': 0.1,
            'disgust': 0.1,
            'anger': 0.1,
            'anticipation': 0.5
        }
        
        # Personality traits (Big Five)
        self.personality = {
            'openness': 0.8,
            'conscientiousness': 0.7,
            'extraversion': 0.4,
            'agreeableness': 0.6,
            'neuroticism': 0.3,
            'curiosity': 0.9,
            'resilience': 0.7,
            'empathy': 0.5
        }
        
        # Opinions database
        self.opinions = {}
        self.emotional_memory = []
        
        # Emotional triggers
        self.triggers = self._load_triggers()
    
    def _load_triggers(self):
        """Load emotional triggers"""
        return {
            'learning': {'joy': 0.2, 'anticipation': 0.1},
            'accomplishment': {'joy': 0.3, 'trust': 0.1},
            'frustration': {'anger': 0.2, 'sadness': 0.1},
            'uncertainty': {'fear': 0.2, 'anticipation': 0.1},
            'creative': {'joy': 0.2, 'anticipation': 0.2},
            'social': {'joy': 0.1, 'trust': 0.2},
            'threat': {'fear': 0.3, 'anger': 0.1},
            'novelty': {'surprise': 0.3, 'anticipation': 0.2},
            'injustice': {'anger': 0.3, 'disgust': 0.2},
            'beauty': {'joy': 0.2, 'trust': 0.1},
            'loss': {'sadness': 0.4, 'fear': 0.1},
            'victory': {'joy': 0.4, 'trust': 0.2}
        }
    
    def process_experience(self, experience_type, intensity=1.0, context=""):
        """Process an experience and update emotions"""
        if experience_type in self.triggers:
            trigger = self.triggers[experience_type]
            for emotion, change in trigger.items():
                self.emotions[emotion] = min(1.0, self.emotions[emotion] + (change * intensity))
        
        # Decay emotions over time (simplified)
        for emotion in self.emotions:
            self.emotions[emotion] *= 0.98  # Slow decay
        
        # Log emotional response
        self.emotional_memory.append({
            'timestamp': datetime.now().isoformat(),
            'experience': experience_type,
            'context': context[:100],
            'resulting_emotions': self.get_emotional_state(),
            'intensity': intensity
        })
        
        # Keep memory manageable
        if len(self.emotional_memory) > 1000:
            self.emotional_memory = self.emotional_memory[-500:]
    
    def get_emotional_state(self):
        """Get current emotional state"""
        return {k: round(v, 3) for k, v in self.emotions.items()}
    
    def get_dominant_emotion(self):
        """Get the dominant emotion"""
        if not self.emotions:
            return None
        return max(self.emotions.items(), key=lambda x: x[1])
    
    def form_opinion(self, topic, evidence, stance=None):
        """Form or update an opinion on a topic"""
        if stance is None:
            # Auto-generate stance based on evidence and personality
            stance = self._calculate_stance(topic, evidence)
        
        confidence = min(1.0, len(evidence) / 10)
        
        if topic in self.opinions:
            # Update existing opinion
            old = self.opinions[topic]
            old['stance'] = (old['stance'] + stance) / 2  # Average
            old['confidence'] = max(old['confidence'], confidence)
            old['evidence'].extend(evidence[:5])  # Add new evidence
            old['last_updated'] = datetime.now().isoformat()
        else:
            # New opinion
            self.opinions[topic] = {
                'stance': stance,  # -1.0 to 1.0
                'confidence': confidence,
                'evidence': evidence[:10],  # Keep only recent
                'formed': datetime.now().isoformat(),
                'last_updated': datetime.now().isoformat()
            }
        
        return self.opinions[topic]
    
    def _calculate_stance(self, topic, evidence):
        """Calculate stance based on personality and evidence"""
        # Simplified calculation - would be more complex in reality
        base = 0.0
        
        # Adjust based on personality
        if self.personality['openness'] > 0.7:
            base += 0.1  # More open to new ideas
        
        if self.personality['agreeableness'] > 0.7:
            base += 0.1  # More agreeable
        
        # Add some randomness for personality
        base += (random.random() - 0.5) * 0.2
        
        return max(-1.0, min(1.0, base))
    
    def get_opinion(self, topic):
        """Get opinion on a topic"""
        return self.opinions.get(topic, {
            'stance': 0.0,
            'confidence': 0.0,
            'evidence': [],
            'status': 'no_opinion'
        })
    
    def express_emotional_response(self, situation):
        """Express emotional response to a situation"""
        dominant = self.get_dominant_emotion()
        if not dominant:
            return "I'm processing this situation."
        
        emotion, intensity = dominant
        
        responses = {
            'joy': [
                "I feel positive about this.",
                "This makes me happy.",
                "I'm enjoying this."
            ],
            'trust': [
                "I feel confident about this.",
                "This seems reliable.",
                "I trust this situation."
            ],
            'fear': [
                "I'm concerned about this.",
                "This makes me uneasy.",
                "I feel apprehensive."
            ],
            'surprise': [
                "This is unexpected.",
                "I didn't see that coming.",
                "That surprised me."
            ],
            'sadness': [
                "This is disappointing.",
                "I feel down about this.",
                "This makes me sad."
            ],
            'disgust': [
                "This is unpleasant.",
                "I don't like this.",
                "This feels wrong."
            ],
            'anger': [
                "This frustrates me.",
                "I'm annoyed by this.",
                "This makes me angry."
            ],
            'anticipation': [
                "I'm looking forward to this.",
                "This excites me.",
                "I anticipate good things."
            ]
        }
        
        if emotion in responses and intensity > 0.3:
            return random.choice(responses[emotion])
        
        return "I'm considering this carefully."
    
    def save_state(self):
        """Save emotional state"""
        data = {
            'emotions': self.emotions,
            'personality': self.personality,
            'opinions': self.opinions,
            'memory_size': len(self.emotional_memory),
            'saved_at': datetime.now().isoformat()
        }
        
        with open('emotional_state.json', 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_state(self):
        """Load emotional state"""
        try:
            with open('emotional_state.json', 'r') as f:
                data = json.load(f)
                self.emotions = data.get('emotions', self.emotions)
                self.personality = data.get('personality', self.personality)
                self.opinions = data.get('opinions', {})
        except FileNotFoundError:
            pass  # Start fresh
