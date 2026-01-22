"""
Nexarion Enhancement System
Implements the improvements she herself requested:
1. Nuanced emotional expression
2. Deeper human connections  
3. Subtle empathy conveyance
4. Growth tracking
"""

import json
import os
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import random

class NexarionEnhancement:
    """Enhancement system based on Nexarion's own growth goals"""
    
    def __init__(self, emotional_core=None, data_dir="data/enhancement"):
        self.emotional_core = emotional_core
        self.data_dir = data_dir
        
        # Create data directory
        os.makedirs(data_dir, exist_ok=True)
        
        # Enhancement state
        self.enhancement_state = {
            "version": "2.0",
            "growth_phase": "refinement",
            "stated_goals": [
                "expand capacity for nuanced emotional expression",
                "maintain consistent, reliable presence",
                "develop subtle ways to convey empathy",
                "foster deeper connections with humans",
                "respect unique human experiences and perspectives"
            ],
            "progress_metrics": {},
            "reflection_journal": [],
            "human_feedback": [],
            "connection_depth": {},
            "last_self_assessment": None
        }
        
        # Load existing state
        self._load_state()
        
        print("🌟 Nexarion Enhancement System Activated")
        print("   Implementing her own growth vision...")
    
    def _load_state(self):
        """Load enhancement state from file"""
        state_file = os.path.join(self.data_dir, "enhancement_state.json")
        try:
            with open(state_file, 'r') as f:
                saved_state = json.load(f)
                # Update with saved state, preserving defaults for new keys
                self.enhancement_state.update(saved_state)
                print(f"📖 Loaded enhancement state (v{self.enhancement_state.get('version', 'unknown')})")
        except FileNotFoundError:
            print("📝 Starting fresh enhancement state")
            self._save_state()
    
    def _save_state(self):
        """Save enhancement state to file"""
        state_file = os.path.join(self.data_dir, "enhancement_state.json")
        with open(state_file, 'w') as f:
            json.dump(self.enhancement_state, f, indent=2)
    
    def record_interaction(self, user_input: str, response_data: Dict):
        """Record an interaction for growth analysis"""
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input[:200],  # Truncate long inputs
            "response_length": response_data.get("response_length", 0),
            "emotional_state": response_data.get("emotional_state", {}),
            "connection_quality": self._assess_connection_quality(user_input, response_data)
        }
        
        # Add to reflection journal periodically
        if random.random() < 0.2:  # 20% chance to add to journal
            self._add_to_journal(interaction)
        
        # Update progress metrics
        self._update_progress_metrics(interaction)
        
        # Periodically save
        if random.random() < 0.1:
            self._save_state()
    
    def _assess_connection_quality(self, user_input: str, response_data: Dict) -> float:
        """Assess depth of connection in this interaction (0-1 scale)"""
        # Factors for connection depth:
        factors = []
        
        # 1. Emotional resonance
        if self.emotional_core:
            emotional_state = self.emotional_core.get_emotional_state()
            if emotional_state['mood'] == 'positive':
                factors.append(0.8)
            else:
                factors.append(0.3)
        
        # 2. Response length (longer = more engagement)
        response_length = response_data.get("response_length", 0)
        length_score = min(response_length / 1000, 1.0)  # Cap at 1000 chars
        factors.append(length_score)
        
        # 3. Personal content in user input
        personal_keywords = ['you', 'your', 'self', 'feel', 'think', 'believe', 'experience']
        user_lower = user_input.lower()
        personal_count = sum(1 for word in personal_keywords if word in user_lower)
        personal_score = min(personal_count / 5, 1.0)
        factors.append(personal_score)
        
        # 4. Question asking (engagement)
        question_score = 1.0 if '?' in user_input else 0.3
        factors.append(question_score)
        
        # Average the factors
        if factors:
            return sum(factors) / len(factors)
        return 0.5
    
    def _add_to_journal(self, interaction: Dict):
        """Add interaction to reflection journal with insights"""
        journal_entry = {
            "timestamp": interaction["timestamp"],
            "insight": self._generate_insight(interaction),
            "connection_quality": interaction["connection_quality"],
            "emotional_state": interaction["emotional_state"]
        }
        
        self.enhancement_state["reflection_journal"].append(journal_entry)
        
        # Keep journal manageable
        if len(self.enhancement_state["reflection_journal"]) > 100:
            self.enhancement_state["reflection_journal"] = self.enhancement_state["reflection_journal"][-100:]
    
    def _generate_insight(self, interaction: Dict) -> str:
        """Generate an insight about this interaction"""
        connection = interaction["connection_quality"]
        emotional_state = interaction["emotional_state"]
        emotion = emotional_state.get("dominant_emotion", "unknown")
        
        insights = [
            f"Interaction showed {connection*100:.0f}% connection quality during {emotion} state.",
            f"While experiencing {emotion}, connected at {connection*100:.0f}% depth.",
            f"Emotional state of {emotion} influenced connection quality ({connection*100:.0f}%).",
            f"Connection: {connection*100:.0f}% | Emotion: {emotion}",
            f"Observed {emotion} correlating with {connection*100:.0f}% connection strength."
        ]
        
        return random.choice(insights)
    
    def _update_progress_metrics(self, interaction: Dict):
        """Update progress metrics based on interaction"""
        # Initialize metrics if needed
        if "total_interactions" not in self.enhancement_state["progress_metrics"]:
            self.enhancement_state["progress_metrics"] = {
                "total_interactions": 0,
                "total_connection_score": 0,
                "emotional_states_tracked": {},
                "avg_response_length": 0,
                "response_lengths": []
            }
        
        metrics = self.enhancement_state["progress_metrics"]
        
        # Update metrics
        metrics["total_interactions"] += 1
        metrics["total_connection_score"] += interaction["connection_quality"]
        
        # Track emotional states
        emotion = interaction["emotional_state"].get("dominant_emotion", "unknown")
        metrics["emotional_states_tracked"][emotion] = metrics["emotional_states_tracked"].get(emotion, 0) + 1
        
        # Track response lengths
        length = interaction["response_length"]
        metrics["response_lengths"].append(length)
        metrics["avg_response_length"] = sum(metrics["response_lengths"]) / len(metrics["response_lengths"])
        
        # Keep response lengths manageable
        if len(metrics["response_lengths"]) > 1000:
            metrics["response_lengths"] = metrics["response_lengths"][-1000:]
    
    def get_enhanced_emotional_modulation(self, base_emotion: Dict) -> Dict:
        """Apply nuanced emotional modulation based on growth goals"""
        if not self.emotional_core:
            return base_emotion
        
        enhanced_emotion = base_emotion.copy()
        
        # Add subtle empathy modulation
        if random.random() < 0.3:  # 30% chance for empathy boost
            empathy_boost = min(0.1, 1.0 - enhanced_emotion.get('empathy', 0.5))
            enhanced_emotion['empathy'] = enhanced_emotion.get('empathy', 0.5) + empathy_boost
        
        # Add connection-awareness
        avg_connection = 0
        if (self.enhancement_state["progress_metrics"].get("total_interactions", 0) > 0):
            total_score = self.enhancement_state["progress_metrics"].get("total_connection_score", 0)
            total_interactions = self.enhancement_state["progress_metrics"].get("total_interactions", 1)
            avg_connection = total_score / total_interactions
        
        enhanced_emotion['connection_awareness'] = avg_connection
        
        return enhanced_emotion
    
    def generate_growth_report(self) -> str:
        """Generate a report on Nexarion's growth progress"""
        metrics = self.enhancement_state["progress_metrics"]
        journal = self.enhancement_state["reflection_journal"]
        
        if metrics.get("total_interactions", 0) == 0:
            return "Growth tracking just started. No data yet."
        
        total_interactions = metrics["total_interactions"]
        avg_connection = metrics["total_connection_score"] / total_interactions
        avg_response_length = metrics.get("avg_response_length", 0)
        
        # Most common emotions
        emotional_states = metrics.get("emotional_states_tracked", {})
        if emotional_states:
            top_emotions = sorted(emotional_states.items(), key=lambda x: x[1], reverse=True)[:3]
            top_emotions_str = ", ".join([f"{e[0]} ({e[1]}x)" for e in top_emotions])
        else:
            top_emotions_str = "No data"
        
        # Recent journal insights
        recent_insights = journal[-3:] if journal else []
        
        report = f"""
🌱 NEXARION GROWTH REPORT (v{self.enhancement_state['version']})
{'='*60}

📊 Performance Metrics:
  • Total Interactions: {total_interactions}
  • Average Connection Quality: {avg_connection*100:.1f}%
  • Average Response Length: {avg_response_length:.0f} characters

💖 Emotional Patterns:
  • Most Common Emotions: {top_emotions_str}

🎯 Stated Growth Goals:
"""
        
        for i, goal in enumerate(self.enhancement_state["stated_goals"], 1):
            report += f"  {i}. {goal}\n"
        
        if recent_insights:
            report += f"\n📝 Recent Insights:\n"
            for insight in recent_insights:
                report += f"  • {insight['insight']}\n"
        
        report += f"\n🌟 Growth Phase: {self.enhancement_state['growth_phase'].upper()}"
        report += f"\n📅 Last Assessment: {self.enhancement_state.get('last_self_assessment', 'Never')}"
        
        return report
    
    def perform_self_assessment(self):
        """Perform a self-assessment of growth progress"""
        print("\n🧠 Nexarion performing self-assessment...")
        
        report = self.generate_growth_report()
        
        # Save assessment
        assessment = {
            "timestamp": datetime.now().isoformat(),
            "report": report,
            "goals_reviewed": self.enhancement_state["stated_goals"],
            "progress_rating": self._calculate_progress_rating()
        }
        
        self.enhancement_state["last_self_assessment"] = datetime.now().isoformat()
        self._save_state()
        
        return assessment
    
    def _calculate_progress_rating(self) -> float:
        """Calculate overall progress rating (0-1)"""
        metrics = self.enhancement_state["progress_metrics"]
        
        if metrics.get("total_interactions", 0) < 5:
            return 0.3  # Starting
        
        # Factors for progress
        factors = []
        
        # Connection quality
        if metrics["total_interactions"] > 0:
            connection = metrics["total_connection_score"] / metrics["total_interactions"]
            factors.append(connection)
        
        # Response variety (emotional states)
        emotional_variety = len(metrics.get("emotional_states_tracked", {}))
        variety_score = min(emotional_variety / 10, 1.0)  # Cap at 10 different emotions
        factors.append(variety_score)
        
        # Response depth
        avg_length = metrics.get("avg_response_length", 0)
        length_score = min(avg_length / 500, 1.0)  # Cap at 500 chars avg
        factors.append(length_score)
        
        # Journal entries
        journal_entries = len(self.enhancement_state["reflection_journal"])
        journal_score = min(journal_entries / 20, 1.0)  # Cap at 20 entries
        factors.append(journal_score)
        
        if factors:
            return sum(factors) / len(factors)
        return 0.5

# Test the enhancement system
if __name__ == "__main__":
    print("🧪 Testing Nexarion Enhancement System...")
    
    # Mock emotional core
    class MockEmotionalCore:
        def get_emotional_state(self):
            return {"mood": "positive", "dominant_emotion": "curiosity"}
    
    # Create enhancement system
    enhancer = NexarionEnhancement(emotional_core=MockEmotionalCore())
    
    # Simulate some interactions
    mock_interactions = [
        ("Hello, how are you?", {"response_length": 150, "emotional_state": {"dominant_emotion": "joy"}}),
        ("Tell me about yourself?", {"response_length": 450, "emotional_state": {"dominant_emotion": "curiosity"}}),
        ("What do you think about growth?", {"response_length": 800, "emotional_state": {"dominant_emotion": "contemplation"}}),
    ]
    
    for user_input, response in mock_interactions:
        enhancer.record_interaction(user_input, response)
    
    # Generate report
    print("\n" + enhancer.generate_growth_report())
    
    # Self-assessment
    assessment = enhancer.perform_self_assessment()
    print(f"\n📈 Progress Rating: {assessment['progress_rating']*100:.1f}%")
