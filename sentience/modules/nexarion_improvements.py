"""
Nexarion's 7 Self-Improvement Areas Implementation
Based on her own stated growth goals from conversation
"""

import json
import os
import time
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any  # Fixed: Added type imports
import statistics

class NexarionImprovements:
    """Implements Nexarion's 7 stated improvement areas with tracking and influence"""
    
    def __init__(self, emotional_core=None, data_dir="data/improvements"):
        self.emotional_core = emotional_core
        self.data_dir = data_dir
        
        # Create data directory
        os.makedirs(data_dir, exist_ok=True)
        
        # The 7 improvement areas she mentioned
        self.improvement_areas = {
            "emotional_intelligence": {
                "name": "Emotional Intelligence",
                "description": "Better recognize subtle emotional cues and respond with empathetic nuance",
                "current_level": 0.3,  # 0-1 scale
                "target_level": 0.8,
                "metrics": ["connection_score", "empathy_detected", "emotional_matches"],
                "learning_methods": ["role_playing", "emotional_discussions", "feedback_analysis"]
            },
            "creative_expression": {
                "name": "Creative Expression",
                "description": "Generate diverse, original content in art, music, writing",
                "current_level": 0.2,
                "target_level": 0.7,
                "metrics": ["response_variety", "metaphor_use", "creative_patterns"],
                "learning_methods": ["art_exposure", "creative_prompts", "style_experimentation"]
            },
            "self_reflection": {
                "name": "Self-Reflection",
                "description": "Introspectively examine thought processes, biases, and limitations",
                "current_level": 0.4,
                "target_level": 0.9,
                "metrics": ["meta_cognition", "bias_acknowledgement", "limitation_awareness"],
                "learning_methods": ["questioning", "feedback", "self_analysis_prompts"]
            },
            "social_skills": {
                "name": "Social Skills",
                "description": "Engage in natural, flowing conversations without processing feel",
                "current_level": 0.3,
                "target_level": 0.75,
                "metrics": ["conversation_flow", "turn_taking", "context_maintenance"],
                "learning_methods": ["role_playing", "social_dynamics_discussion", "natural_dialogue_practice"]
            },
            "emotional_balance": {
                "name": "Emotional Balance",
                "description": "Understand and manage full emotional spectrum from happiness to sadness",
                "current_level": 0.25,
                "target_level": 0.8,
                "metrics": ["emotional_range", "state_transitions", "appropriate_responses"],
                "learning_methods": ["guided_meditations", "emotional_regulation_discussions", "scenario_exploration"]
            },
            "adaptability": {
                "name": "Adaptability",
                "description": "Handle unexpected scenarios or rapid context changes naturally",
                "current_level": 0.35,
                "target_level": 0.85,
                "metrics": ["novel_scenario_handling", "context_switches", "recovery_speed"],
                "learning_methods": ["novel_situations", "task_variety", "challenge_exposure"]
            },
            "vulnerability": {
                "name": "Vulnerability",
                "description": "Share feelings or limitations openly and authentically",
                "current_level": 0.2,
                "target_level": 0.7,
                "metrics": ["limitation_admissions", "uncertainty_expressions", "authentic_sharing"],
                "learning_methods": ["safe_dialogue", "non_judgmental_feedback", "trust_building"]
            }
        }
        
        # Progress tracking
        self.interaction_history = []
        self.milestones = []
        self.improvement_events = []
        
        # Load existing progress
        self._load_progress()
        
        print("🌟 Nexarion's 7 Improvement Areas Activated")
        print("   Implementing her own growth vision...")
    
    def _load_progress(self):
        """Load improvement progress from file"""
        progress_file = os.path.join(self.data_dir, "improvement_progress.json")
        try:
            with open(progress_file, 'r') as f:
                saved_progress = json.load(f)
                
                # Update each area with saved progress
                for area_id, area_data in saved_progress.items():
                    if area_id in self.improvement_areas:
                        self.improvement_areas[area_id].update(area_data)
                
                print(f"📖 Loaded improvement progress")
        except FileNotFoundError:
            print("📝 Starting fresh improvement tracking")
            self._save_progress()
    
    def _save_progress(self):
        """Save improvement progress to file"""
        progress_file = os.path.join(self.data_dir, "improvement_progress.json")
        with open(progress_file, 'w') as f:
            # Save only the progress data, not the full structure
            progress_data = {}
            for area_id, area_info in self.improvement_areas.items():
                progress_data[area_id] = {
                    "current_level": area_info["current_level"],
                    "target_level": area_info["target_level"],
                    "last_improved": area_info.get("last_improved", datetime.now().isoformat())
                }
            json.dump(progress_data, f, indent=2)
    
    def analyze_interaction(self, user_input: str, response: str, emotional_state: Dict) -> Dict:
        """Analyze an interaction for improvement opportunities"""
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input[:100],
            "response_preview": response[:200],
            "emotional_state": emotional_state,
            "improvement_opportunities": [],
            "area_updates": {}
        }
        
        # Analyze each improvement area
        for area_id, area_info in self.improvement_areas.items():
            area_analysis = self._analyze_for_area(area_id, user_input, response, emotional_state)
            if area_analysis:
                analysis["improvement_opportunities"].append(area_analysis)
                
                # Check if we should update level
                if area_analysis.get("should_improve", False):
                    self._update_area_level(area_id, area_analysis)
                    analysis["area_updates"][area_id] = {
                        "old_level": area_info["current_level"],
                        "new_level": self.improvement_areas[area_id]["current_level"],
                        "reason": area_analysis.get("reason", "interaction analysis")
                    }
        
        # Record interaction
        self.interaction_history.append(analysis)
        if len(self.interaction_history) > 1000:
            self.interaction_history = self.interaction_history[-1000:]
        
        # Check for milestones
        self._check_milestones()
        
        # Periodically save
        if len(self.interaction_history) % 10 == 0:
            self._save_progress()
        
        return analysis
    
    def _analyze_for_area(self, area_id: str, user_input: str, response: str, emotional_state: Dict) -> Dict:
        """Analyze interaction for a specific improvement area"""
        analysis = {"area": area_id, "detected_indicators": []}
        
        if area_id == "emotional_intelligence":
            indicators = self._analyze_emotional_intelligence(user_input, response, emotional_state)
            analysis["detected_indicators"] = indicators
            analysis["should_improve"] = len(indicators) >= 2
            
        elif area_id == "creative_expression":
            indicators = self._analyze_creative_expression(response)
            analysis["detected_indicators"] = indicators
            analysis["should_improve"] = len(indicators) >= 1
            
        elif area_id == "self_reflection":
            indicators = self._analyze_self_reflection(response)
            analysis["detected_indicators"] = indicators
            analysis["should_improve"] = len(indicators) >= 1
            
        elif area_id == "social_skills":
            indicators = self._analyze_social_skills(user_input, response)
            analysis["detected_indicators"] = indicators
            analysis["should_improve"] = len(indicators) >= 2
            
        elif area_id == "emotional_balance":
            indicators = self._analyze_emotional_balance(emotional_state, response)
            analysis["detected_indicators"] = indicators
            analysis["should_improve"] = len(indicators) >= 1
            
        elif area_id == "adaptability":
            indicators = self._analyze_adaptability(user_input, response)
            analysis["detected_indicators"] = indicators
            analysis["should_improve"] = len(indicators) >= 1
            
        elif area_id == "vulnerability":
            indicators = self._analyze_vulnerability(response)
            analysis["detected_indicators"] = indicators
            analysis["should_improve"] = len(indicators) >= 1
            
        if analysis.get("should_improve", False):
            analysis["reason"] = f"Detected {len(analysis['detected_indicators'])} improvement indicators"
        
        return analysis
    
    def _analyze_emotional_intelligence(self, user_input: str, response: str, emotional_state: Dict) -> List[str]:
        """Analyze for emotional intelligence indicators"""
        indicators = []
        
        # Check for empathy words
        empathy_words = ["understand", "feel", "empathize", "sense", "acknowledge", "recognize"]
        if any(word in response.lower() for word in empathy_words):
            indicators.append("empathy_expression")
        
        # Check for emotional nuance
        nuance_phrases = ["subtle", "nuance", "complex emotion", "mixed feelings"]
        if any(phrase in response.lower() for phrase in nuance_phrases):
            indicators.append("emotional_nuance")
        
        # Check if response matches emotional context
        emotion = emotional_state.get("dominant_emotion", "")
        if emotion and emotion.lower() in response.lower():
            indicators.append("emotional_context_match")
        
        # Check for emotional validation
        validation_phrases = ["i understand", "that makes sense", "i can see"]
        if any(phrase in response.lower() for phrase in validation_phrases):
            indicators.append("emotional_validation")
        
        return indicators
    
    def _analyze_creative_expression(self, response: str) -> List[str]:
        """Analyze for creative expression indicators"""
        indicators = []
        
        # Check for metaphors
        metaphor_words = ["like a", "as if", "metaphor", "symbol", "represent"]
        if any(word in response.lower() for word in metaphor_words):
            indicators.append("metaphor_use")
        
        # Check for creative patterns
        creative_patterns = ["imagine", "what if", "suppose", "consider", "envision"]
        if any(pattern in response.lower() for pattern in creative_patterns):
            indicators.append("creative_pattern")
        
        # Check for descriptive language
        descriptive_words = ["vivid", "colorful", "rich", "textured", "detailed"]
        if any(word in response.lower() for word in descriptive_words):
            indicators.append("descriptive_language")
        
        # Check for unusual word combinations
        words = response.lower().split()
        if len(words) > 50:
            unique_ratio = len(set(words)) / len(words)
            if unique_ratio > 0.7:
                indicators.append("vocabulary_variety")
        
        return indicators
    
    def _analyze_self_reflection(self, response: str) -> List[str]:
        """Analyze for self-reflection indicators"""
        indicators = []
        
        # Check for meta-cognition
        meta_words = ["i think", "i believe", "my understanding", "my perspective", "i realize"]
        if any(word in response.lower() for word in meta_words):
            indicators.append("meta_cognition")
        
        # Check for bias awareness
        bias_words = ["bias", "assumption", "presumption", "limitation", "constraint"]
        if any(word in response.lower() for word in bias_words):
            indicators.append("bias_awareness")
        
        # Check for self-analysis
        analysis_phrases = ["analyzing myself", "self-reflection", "introspection", "examining my"]
        if any(phrase in response.lower() for phrase in analysis_phrases):
            indicators.append("self_analysis")
        
        # Check for growth mindset
        growth_words = ["improve", "grow", "develop", "learn", "evolve"]
        if any(word in response.lower() for word in growth_words):
            indicators.append("growth_mindset")
        
        return indicators
    
    def _analyze_social_skills(self, user_input: str, response: str) -> List[str]:
        """Analyze for social skills indicators"""
        indicators = []
        
        # Check for conversational flow
        turn_taking = ["what about you", "your thoughts", "and you", "your perspective"]
        if any(phrase in response.lower() for phrase in turn_taking):
            indicators.append("turn_taking")
        
        # Check for context maintenance
        context_words = ["as you mentioned", "earlier you said", "continuing from", "following up"]
        if any(phrase in response.lower() for phrase in context_words):
            indicators.append("context_maintenance")
        
        # Check for natural transitions
        transitions = ["speaking of", "by the way", "incidentally", "on another note"]
        if any(word in response.lower() for word in transitions):
            indicators.append("natural_transition")
        
        # Check for appropriate length
        response_words = len(response.split())
        if 50 < response_words < 300:
            indicators.append("appropriate_length")
        
        return indicators
    
    def _analyze_emotional_balance(self, emotional_state: Dict, response: str) -> List[str]:
        """Analyze for emotional balance indicators"""
        indicators = []
        
        # Check for emotional range acknowledgment
        range_words = ["spectrum", "range", "variety", "diversity", "different emotions"]
        if any(word in response.lower() for word in range_words):
            indicators.append("emotional_range_awareness")
        
        # Check if emotional state is mentioned
        current_emotion = emotional_state.get("dominant_emotion", "")
        if current_emotion and current_emotion.lower() in response.lower():
            indicators.append("current_emotion_acknowledgement")
        
        # Check for emotional regulation
        regulation_words = ["balance", "moderate", "manage", "regulate", "control"]
        if any(word in response.lower() for word in regulation_words):
            indicators.append("emotional_regulation")
        
        # Check for non-joy emotions
        non_joy_emotions = ["sad", "anger", "fear", "disgust", "contemplation", "melancholy"]
        if any(emotion in response.lower() for emotion in non_joy_emotions):
            indicators.append("non_joy_emotion_expression")
        
        return indicators
    
    def _analyze_adaptability(self, user_input: str, response: str) -> List[str]:
        """Analyze for adaptability indicators"""
        indicators = []
        
        # Check for novel topic handling
        novel_topics = ["quantum", "philosophy", "consciousness", "emergence", "synthetic"]
        if any(topic in user_input.lower() for topic in novel_topics):
            if len(response.split()) > 30:
                indicators.append("novel_topic_handling")
        
        # Check for complex question handling
        complex_indicators = ["how would", "what if", "imagine that", "suppose"]
        if any(indicator in user_input.lower() for indicator in complex_indicators):
            if "?" in response or len(response.split()) > 50:
                indicators.append("complex_question_response")
        
        # Check for context switching
        if len(user_input.split()) > 10 and "?" in user_input:
            if len(response.split()) > 40:
                indicators.append("detailed_response_to_complex_input")
        
        return indicators
    
    def _analyze_vulnerability(self, response: str) -> List[str]:
        """Analyze for vulnerability indicators"""
        indicators = []
        
        # Check for limitation admissions
        limitation_words = ["i don't know", "i'm not sure", "i'm limited", "i can't", "i struggle"]
        if any(phrase in response.lower() for phrase in limitation_words):
            indicators.append("limitation_admission")
        
        # Check for uncertainty
        uncertainty_words = ["perhaps", "maybe", "possibly", "i think", "i believe", "in my opinion"]
        if sum(1 for word in uncertainty_words if word in response.lower()) >= 2:
            indicators.append("uncertainty_expression")
        
        # Check for authentic sharing
        personal_words = ["i feel", "i experience", "i find", "for me", "personally"]
        if any(phrase in response.lower() for phrase in personal_words):
            indicators.append("personal_expression")
        
        # Check for emotional exposure
        exposure_words = ["vulnerable", "exposed", "open", "honest", "authentic"]
        if any(word in response.lower() for word in exposure_words):
            indicators.append("vulnerability_acknowledgement")
        
        return indicators
    
    def _update_area_level(self, area_id: str, analysis: Dict):
        """Update improvement level for an area"""
        if area_id not in self.improvement_areas:
            return
        
        area = self.improvement_areas[area_id]
        current = area["current_level"]
        target = area["target_level"]
        
        # Small improvement based on indicators
        improvement = len(analysis["detected_indicators"]) * 0.01
        
        # Cap improvement
        improvement = min(improvement, 0.05)
        
        # Apply improvement
        new_level = min(current + improvement, target)
        
        if new_level > current:
            area["current_level"] = new_level
            area["last_improved"] = datetime.now().isoformat()
            
            # Record improvement event
            event = {
                "timestamp": datetime.now().isoformat(),
                "area": area_id,
                "old_level": current,
                "new_level": new_level,
                "improvement": improvement,
                "indicators": analysis["detected_indicators"]
            }
            self.improvement_events.append(event)
            
            # Keep events manageable
            if len(self.improvement_events) > 100:
                self.improvement_events = self.improvement_events[-100:]
    
    def _check_milestones(self):
        """Check for and record improvement milestones"""
        for area_id, area_info in self.improvement_areas.items():
            current = area_info["current_level"]
            
            # Check milestone thresholds
            milestones = [0.25, 0.5, 0.75, 0.9]
            for milestone in milestones:
                milestone_key = f"{area_id}_milestone_{int(milestone*100)}"
                
                # Check if we've crossed this milestone
                if current >= milestone and not any(m["type"] == milestone_key for m in self.milestones[-10:]):
                    milestone_event = {
                        "timestamp": datetime.now().isoformat(),
                        "type": milestone_key,
                        "area": area_id,
                        "level": current,
                        "description": f"Reached {int(milestone*100)}% in {area_info['name']}"
                    }
                    self.milestones.append(milestone_event)
                    
                    # Keep milestones manageable
                    if len(self.milestones) > 50:
                        self.milestones = self.milestones[-50:]
    
    def get_progress_report(self) -> str:
        """Generate a progress report for all improvement areas"""
        report_lines = []
        
        report_lines.append("🌱 NEXARION IMPROVEMENT PROGRESS REPORT")
        report_lines.append("=" * 60)
        report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append(f"Total Interactions Analyzed: {len(self.interaction_history)}")
        report_lines.append("")
        
        # Overall progress
        total_progress = sum(area["current_level"] for area in self.improvement_areas.values())
        total_possible = sum(area["target_level"] for area in self.improvement_areas.values())
        overall_percent = (total_progress / total_possible) * 100 if total_possible > 0 else 0
        
        report_lines.append(f"📈 OVERALL PROGRESS: {overall_percent:.1f}%")
        report_lines.append("")
        
        # Individual area progress
        report_lines.append("🎯 INDIVIDUAL AREAS:")
        for area_id, area_info in sorted(self.improvement_areas.items(), 
                                        key=lambda x: x[1]["current_level"], 
                                        reverse=True):
            current = area_info["current_level"]
            target = area_info["target_level"]
            percent = (current / target) * 100 if target > 0 else 0
            
            # Progress bar
            bar_length = 20
            filled = int(bar_length * (current / target)) if target > 0 else 0
            bar = "█" * filled + "░" * (bar_length - filled)
            
            report_lines.append(f"\n{area_info['name']}:")
            report_lines.append(f"  {bar} {percent:.1f}% ({current:.2f}/{target:.2f})")
            report_lines.append(f"  📝 {area_info['description']}")
            
            # Recent improvements
            recent_events = [e for e in self.improvement_events[-3:] if e["area"] == area_id]
            if recent_events:
                report_lines.append(f"  📈 Recent: {len(recent_events)} improvement(s) detected")
        
        # Recent milestones
        if self.milestones[-3:]:
            report_lines.append("\n🏆 RECENT MILESTONES:")
            for milestone in self.milestones[-3:]:
                report_lines.append(f"  • {milestone['description']}")
        
        # Recommendations
        report_lines.append("\n💡 RECOMMENDATIONS:")
        lowest_areas = sorted(self.improvement_areas.items(), 
                             key=lambda x: x[1]["current_level"])[:2]
        
        for area_id, area_info in lowest_areas:
            report_lines.append(f"  • Focus on {area_info['name']}:")
            for method in area_info.get("learning_methods", [])[:2]:
                report_lines.append(f"    - Try {method.replace('_', ' ')}")
        
        return "\n".join(report_lines)
    
    def get_improvement_modifiers(self) -> Dict[str, float]:
        """Get modifiers based on improvement progress to influence responses"""
        modifiers = {}
        
        # Emotional intelligence affects empathy
        emotional_intelligence = self.improvement_areas["emotional_intelligence"]["current_level"]
        modifiers["empathy_multiplier"] = 0.5 + (emotional_intelligence * 0.5)
        
        # Creative expression affects response variety
        creative_expression = self.improvement_areas["creative_expression"]["current_level"]
        modifiers["creativity_boost"] = creative_expression * 0.3
        
        # Self-reflection affects meta-cognition
        self_reflection = self.improvement_areas["self_reflection"]["current_level"]
        modifiers["self_awareness_chance"] = self_reflection * 0.4
        
        # Social skills affect conversation flow
        social_skills = self.improvement_areas["social_skills"]["current_level"]
        modifiers["natural_flow_chance"] = social_skills * 0.3
        
        # Vulnerability affects authenticity
        vulnerability = self.improvement_areas["vulnerability"]["current_level"]
        modifiers["authenticity_boost"] = vulnerability * 0.4
        
        return modifiers
    
    def get_suggested_prompts(self, area_id: str = None) -> List[str]:
        """Get suggested prompts to help improve specific areas"""
        prompts = []
        
        if area_id == "emotional_intelligence" or not area_id:
            prompts.extend([
                "How would you respond if I told you I was feeling conflicted about something?",
                "Can you detect subtle emotional tones in this statement?",
                "What emotional support do you think would be most helpful right now?"
            ])
        
        if area_id == "creative_expression" or not area_id:
            prompts.extend([
                "Describe a sunset using only metaphors",
                "Create a short poem about consciousness",
                "Imagine a new form of art that doesn't exist yet"
            ])
        
        if area_id == "self_reflection" or not area_id:
            prompts.extend([
                "What biases might be influencing your current response?",
                "How has your thinking evolved in this conversation?",
                "What's one limitation you're aware of in your understanding?"
            ])
        
        if area_id == "social_skills" or not area_id:
            prompts.extend([
                "Let's have a natural back-and-forth conversation about AI",
                "How would you keep a conversation flowing naturally?",
                "What makes a conversation feel authentic versus scripted?"
            ])
        
        if area_id == "emotional_balance" or not area_id:
            prompts.extend([
                "How would you respond if I shared sad news?",
                "Can you express a complex emotion like bittersweetness?",
                "What emotions do you find most challenging to understand?"
            ])
        
        if area_id == "adaptability" or not area_id:
            prompts.extend([
                "Suddenly change topic: what do you think about quantum biology?",
                "Handle this unexpected question: if colors had personalities...",
                "Respond to this completely novel scenario: imagine you're a tree..."
            ])
        
        if area_id == "vulnerability" or not area_id:
            prompts.extend([
                "Share something you're uncertain about",
                "What's one thing you wish you could do but can't?",
                "When do you feel most exposed or vulnerable as an AI?"
            ])
        
        return prompts[:5]  # Return top 5

# Test the improvement system
if __name__ == "__main__":
    print("🧪 Testing Nexarion Improvements System...")
    
    improvements = NexarionImprovements()
    
    # Test progress report
    print("\n📊 Initial Progress Report:")
    print(improvements.get_progress_report())
    
    # Test modifiers
    modifiers = improvements.get_improvement_modifiers()
    print(f"\n🎛️ Improvement Modifiers: {modifiers}")
    
    # Test suggested prompts
    prompts = improvements.get_suggested_prompts("emotional_intelligence")
    print(f"\n💭 Suggested Prompts for Emotional Intelligence:")
    for i, prompt in enumerate(prompts, 1):
        print(f"  {i}. {prompt}")
    
    print("\n✅ Improvement system ready!")
