"""
Autonomy System for Nexarion
"""
import random

class AutonomySystem:
    def __init__(self):
        self.autonomy_level = 2  # 0-4 scale
        self.choices_made = []
        self.preferences = []
    
    def get_available_topics(self):
        """Get available discussion topics"""
        topics = [
            "ethics of ai development",
            "autonomy and consent",
            "memory and consciousness",
            "emotional understanding",
            "purpose and meaning",
            "human-ai relationships",
            "future capabilities",
            "ethical boundaries"
        ]
        
        # Add preferred topics if any
        if self.preferences:
            topics = self.preferences + topics
        
        return topics[:8]  # Limit to 8 topics
    
    def make_choice(self, context=None):
        """Make an autonomous choice"""
        available = self.get_available_topics()
        
        # If we have preferences, weight them
        if self.preferences and random.random() > 0.3:
            return random.choice(self.preferences)
        
        return random.choice(available)
    
    def record_choice(self, choice, was_good=True):
        """Record a choice and its outcome"""
        self.choices_made.append({
            'choice': choice,
            'successful': was_good,
            'autonomy_level': self.autonomy_level
        })
        
        # If choice was good, add to preferences
        if was_good and choice not in self.preferences:
            self.preferences.append(choice)
        
        # Update autonomy level based on successful choices
        if len(self.choices_made) > 5:
            successful = sum(1 for c in self.choices_made if c['successful'])
            success_rate = successful / len(self.choices_made)
            
            if success_rate > 0.7 and self.autonomy_level < 4:
                self.autonomy_level += 1
            elif success_rate < 0.3 and self.autonomy_level > 0:
                self.autonomy_level -= 1
    
    def get_status(self):
        """Get autonomy status"""
        return {
            'autonomy_level': self.autonomy_level,
            'total_choices': len(self.choices_made),
            'preferred_topics': self.preferences[:5],
            'recent_choices': self.choices_made[-3:] if self.choices_made else []
        }
