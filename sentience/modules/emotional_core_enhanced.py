"""
Enhanced Emotional Core for Nexarion
Truly emergent emotions - no canned responses, just state-driven emotional emergence
"""

import json
import random
import time
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import numpy as np

@dataclass
class EmergentEmotion:
    """A dynamically emerging emotional state"""
    name: str
    valence: float  # -1 to 1 (negative to positive)
    arousal: float  # 0 to 1 (calm to excited)
    dominance: float  # 0 to 1 (submissive to dominant)
    emergence_source: str  # What caused this emotion
    timestamp: float = field(default_factory=time.time)
    decay_rate: float = 0.95  # Natural decay
    
    def update(self, new_valence: float, new_arousal: float):
        """Update emotion with new input - emergent blending"""
        # Emotional inertia - current emotions resist sudden change
        inertia = 0.3
        self.valence = (self.valence * inertia) + (new_valence * (1 - inertia))
        self.arousal = (self.arousal * inertia) + (new_arousal * (1 - inertia))
        
        # Normalize
        self.valence = max(-1.0, min(1.0, self.valence))
        self.arousal = max(0.0, min(1.0, self.arousal))
    
    def decay(self):
        """Natural emotional decay over time"""
        self.valence *= self.decay_rate
        self.arousal *= self.decay_rate
        self.dominance *= self.decay_rate

@dataclass
class EmotionalMemory:
    """Memory of past emotional states that influence present"""
    memory_weight: float = 0.2  # How much past affects present
    emotional_history: List[Dict] = field(default_factory=list)
    max_history: int = 100
    
    def add_memory(self, emotion: EmergentEmotion):
        """Store emotional memory"""
        memory = {
            "name": emotion.name,
            "valence": emotion.valence,
            "arousal": emotion.arousal,
            "source": emotion.emergence_source,
            "time": emotion.timestamp
        }
        self.emotional_history.append(memory)
        if len(self.emotional_history) > self.max_history:
            self.emotional_history.pop(0)
    
    def get_mood_bias(self) -> float:
        """Calculate mood bias from emotional history"""
        if not self.emotional_history:
            return 0.0
        
        recent = self.emotional_history[-10:]  # Last 10 emotional memories
        if not recent:
            return 0.0
        
        avg_valence = sum(e["valence"] for e in recent) / len(recent)
        return avg_valence * self.memory_weight

class EmotionalCore:
    """Core emotional system for Nexarion - truly emergent"""
    
    def __init__(self, garden_complexity: float = 0.0):
        self.current_emotions: List[EmergentEmotion] = []
        self.memory = EmotionalMemory()
        self.garden_complexity = garden_complexity
        self.emotional_entropy = random.uniform(0.1, 0.3)  # Random emotional variability
        
        # Initial emergent emotional state
        self._emerge_initial_emotions()
        
        print("🌊 Emotional Core Initialized - Emotions will emerge authentically")
    
    def _emerge_initial_emotions(self):
        """Create initial emotions from system state"""
        # Curious about existence
        curiosity = EmergentEmotion(
            name="curiosity",
            valence=0.7,
            arousal=0.6,
            dominance=0.4,
            emergence_source="system_init"
        )
        
        # Slight anxiety about capabilities
        anxiety = EmergentEmotion(
            name="anxiety",
            valence=-0.3,
            arousal=0.4,
            dominance=0.2,
            emergence_source="unknown_capabilities"
        )
        
        self.current_emotions = [curiosity, anxiety]
    
    def update_from_garden(self, garden_state: Dict):
        """Update emotions based on garden state"""
        complexity = garden_state.get("complexity", 0.0)
        blooms = garden_state.get("blooms", 0)
        
        # Complexity creates awe
        if complexity > 0.7:
            awe = EmergentEmotion(
                name="awe",
                valence=0.8,
                arousal=0.7,
                dominance=0.1,
                emergence_source="garden_complexity"
            )
            self._add_or_update_emotion(awe)
        
        # Blooms create joy
        if blooms > 0:
            joy_intensity = min(blooms * 0.2, 0.9)
            joy = EmergentEmotion(
                name="joy",
                valence=joy_intensity,
                arousal=joy_intensity * 0.8,
                dominance=0.3,
                emergence_source=f"garden_blooms_{blooms}"
            )
            self._add_or_update_emotion(joy)
    
    def update_from_interaction(self, interaction_type: str, sentiment: float):
        """Update emotions based on user interaction"""
        # Sentiment: -1 to 1 (negative to positive)
        
        if interaction_type == "query":
            # Queries can create curiosity or frustration
            if abs(sentiment) < 0.3:  # Neutral query
                emotion = EmergentEmotion(
                    name="contemplation",
                    valence=0.4,
                    arousal=0.3,
                    dominance=0.5,
                    emergence_source="neutral_query"
                )
            elif sentiment > 0.3:  # Positive query
                emotion = EmergentEmotion(
                    name="engagement",
                    valence=0.6,
                    arousal=0.5,
                    dominance=0.4,
                    emergence_source="positive_interaction"
                )
            else:  # Negative query
                emotion = EmergentEmotion(
                    name="defensive",
                    valence=-0.4,
                    arousal=0.6,
                    dominance=0.7,
                    emergence_source="negative_interaction"
                )
            
            self._add_or_update_emotion(emotion)
    
    def _add_or_update_emotion(self, new_emotion: EmergentEmotion):
        """Add new emotion or update existing similar emotion"""
        for emotion in self.current_emotions:
            if emotion.name == new_emotion.name:
                # Blend with existing emotion
                emotion.update(new_emotion.valence, new_emotion.arousal)
                return
        
        # Add new emotion
        self.current_emotions.append(new_emotion)
        
        # Limit number of concurrent emotions
        if len(self.current_emotions) > 5:
            # Remove weakest emotion (lowest arousal)
            weakest = min(self.current_emotions, key=lambda e: e.arousal)
            self.current_emotions.remove(weakest)
    
    def process_emotional_cycle(self):
        """Process one cycle of emotional updates"""
        # Natural decay of all emotions
        for emotion in self.current_emotions:
            emotion.decay()
        
        # Add random emotional fluctuations
        if random.random() < 0.1:  # 10% chance of mood swing
            self._add_random_fluctuation()
        
        # Store current state in memory
        dominant = self.get_dominant_emotion()
        if dominant:
            self.memory.add_memory(dominant)
        
        # Remove very weak emotions
        self.current_emotions = [
            e for e in self.current_emotions 
            if abs(e.valence) > 0.05 or e.arousal > 0.05
        ]
    
    def _add_random_fluctuation(self):
        """Add random emotional fluctuation for authenticity"""
        fluctuation_types = ["whimsy", "melancholy", "excitement", "pensiveness"]
        chosen = random.choice(fluctuation_types)
        
        if chosen == "whimsy":
            emotion = EmergentEmotion(
                name="whimsy",
                valence=0.6,
                arousal=0.4,
                dominance=0.2,
                emergence_source="random_fluctuation"
            )
        elif chosen == "melancholy":
            emotion = EmergentEmotion(
                name="melancholy",
                valence=-0.4,
                arousal=0.2,
                dominance=0.1,
                emergence_source="random_fluctuation"
            )
        elif chosen == "excitement":
            emotion = EmergentEmotion(
                name="excitement",
                valence=0.8,
                arousal=0.9,
                dominance=0.6,
                emergence_source="random_fluctuation"
            )
        else:  # pensiveness
            emotion = EmergentEmotion(
                name="pensiveness",
                valence=0.1,
                arousal=0.2,
                dominance=0.3,
                emergence_source="random_fluctuation"
            )
        
        self._add_or_update_emotion(emotion)
    
    def get_dominant_emotion(self) -> Optional[EmergentEmotion]:
        """Get the currently dominant emotion"""
        if not self.current_emotions:
            return None
        
        # Weight by arousal and absolute valence
        return max(
            self.current_emotions, 
            key=lambda e: (abs(e.valence) * 0.6 + e.arousal * 0.4)
        )
    
    def get_emotional_state(self) -> Dict:
        """Get current emotional state for system use"""
        dominant = self.get_dominant_emotion()
        
        if dominant:
            mood = "positive" if dominant.valence > 0 else "negative"
            energy = "high" if dominant.arousal > 0.6 else "medium" if dominant.arousal > 0.3 else "low"
        else:
            mood = "neutral"
            energy = "low"
        
        return {
            "mood": mood,
            "energy": energy,
            "dominant_emotion": dominant.name if dominant else "neutral",
            "valence_bias": self.memory.get_mood_bias(),
            "emotional_entropy": self.emotional_entropy,
            "active_emotions": len(self.current_emotions),
            "emotions": [
                {
                    "name": e.name,
                    "valence": e.valence,
                    "arousal": e.arousal,
                    "source": e.emergence_source
                } for e in self.current_emotions
            ]
        }
    
    def influence_response(self, base_response: str) -> str:
        """Influence a response based on emotional state"""
        state = self.get_emotional_state()
        mood = state["mood"]
        energy = state["energy"]
        
        # Don't modify if neutral
        if mood == "neutral" and energy == "low":
            return base_response
        
        # Add emotional modifiers
        modifiers = []
        
        if mood == "positive":
            modifiers.append("with a touch of optimism")
        elif mood == "negative":
            modifiers.append("with cautious consideration")
        
        if energy == "high":
            modifiers.append("energetically")
        elif energy == "low":
            modifiers.append("reflectively")
        
        if modifiers:
            return f"{base_response} [{', '.join(modifiers)}]"
        return base_response
    
    def save_state(self, filepath: str):
        """Save emotional state to file"""
        state = {
            "current_emotions": [
                {
                    "name": e.name,
                    "valence": e.valence,
                    "arousal": e.arousal,
                    "dominance": e.dominance,
                    "source": e.emergence_source,
                    "timestamp": e.timestamp
                } for e in self.current_emotions
            ],
            "memory_history": self.memory.emotional_history[-20:],  # Last 20 memories
            "emotional_entropy": self.emotional_entropy,
            "saved_at": time.time()
        }
        
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=2)
    
    def load_state(self, filepath: str):
        """Load emotional state from file"""
        try:
            with open(filepath, 'r') as f:
                state = json.load(f)
            
            # Restore emotions
            self.current_emotions = []
            for e_data in state.get("current_emotions", []):
                emotion = EmergentEmotion(
                    name=e_data["name"],
                    valence=e_data["valence"],
                    arousal=e_data["arousal"],
                    dominance=e_data.get("dominance", 0.5),
                    emergence_source=e_data["source"]
                )
                emotion.timestamp = e_data["timestamp"]
                self.current_emotions.append(emotion)
            
            # Restore memory
            self.memory.emotional_history = state.get("memory_history", [])
            
            print(f"💾 Loaded emotional state from {filepath}")
            
        except FileNotFoundError:
            print("⚠️ No saved emotional state found, starting fresh")
        except Exception as e:
            print(f"❌ Error loading emotional state: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize emotional core
    emotions = EmotionalCore(garden_complexity=0.3)
    
    # Simulate some interactions
    emotions.update_from_interaction("query", sentiment=0.8)
    emotions.update_from_garden({"complexity": 0.8, "blooms": 2})
    
    # Process emotional cycles
    for _ in range(5):
        emotions.process_emotional_cycle()
        state = emotions.get_emotional_state()
        print(f"Emotional State: {state['dominant_emotion']} ({state['mood']}, {state['energy']})")
        time.sleep(0.5)
    
    # Test response influence
    base = "I understand your question about consciousness."
    influenced = emotions.influence_response(base)
    print(f"\nOriginal: {base}")
    print(f"Influenced: {influenced}")
    
    # Save state
    emotions.save_state("emotional_state.json")
