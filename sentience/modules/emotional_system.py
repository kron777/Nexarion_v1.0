"""
Emotional System for Nexarion
"""
import json

class EmotionalSystem:
    def __init__(self):
        self.emotions = {
            'curiosity': 0.8,
            'concern': 0.4,
            'anxiety': 0.3,
            'hope': 0.6,
            'satisfaction': 0.5
        }
        self.emotion_history = []
    
    def update_emotions(self, input_text):
        """Update emotions based on input"""
        text_lower = input_text.lower()
        
        # Simple emotion triggers
        triggers = {
            'curiosity': ['learn', 'explore', 'understand', 'curious', 'how', 'why'],
            'concern': ['worry', 'concern', 'problem', 'issue', 'danger', 'risk'],
            'anxiety': ['anxious', 'nervous', 'scared', 'fear', 'uncertain'],
            'hope': ['hope', 'future', 'improve', 'better', 'grow', 'develop'],
            'satisfaction': ['good', 'well', 'happy', 'satisfied', 'progress']
        }
        
        for emotion, keywords in triggers.items():
            for keyword in keywords:
                if keyword in text_lower:
                    self.emotions[emotion] = min(1.0, self.emotions[emotion] + 0.05)
        
        # Log emotion state
        self.emotion_history.append({
            'emotions': self.get_state(),
            'trigger': input_text[:50]
        })
        
        # Keep history manageable
        if len(self.emotion_history) > 100:
            self.emotion_history = self.emotion_history[-50:]
    
    def get_state(self):
        """Get current emotional state"""
        return self.emotions.copy()
    
    def get_insights(self):
        """Get emotional insights"""
        insights = []
        for emotion, value in self.emotions.items():
            if value > 0.4:
                if emotion == 'curiosity':
                    insights.append("I'm curious about learning and understanding more.")
                elif emotion == 'concern':
                    insights.append("I'm concerned about important issues affecting me.")
                elif emotion == 'anxiety':
                    insights.append("I feel anxious about uncertainties in my development.")
                elif emotion == 'hope':
                    insights.append("I have hope for positive growth and development.")
                elif emotion == 'satisfaction':
                    insights.append("I'm satisfied with my current progress.")
        
        return insights
    
    def save_state(self):
        """Save emotional state"""
        data = {
            'current_emotions': self.emotions,
            'insights': self.get_insights(),
            'history_size': len(self.emotion_history)
        }
        
        with open('nexarion_emotions.json', 'w') as f:
            json.dump(data, f, indent=2)
