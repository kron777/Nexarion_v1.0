"""
Unified Nexarion with 7 Improvement Areas Integration
Implements her own stated growth goals with real-time tracking and influence
"""

import asyncio
import json
import sys
import os
import random
from datetime import datetime
from typing import Dict, List, Optional, Any  # Fixed: Added type imports

# Add the project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, project_root)

try:
    from sentience.modules.emotional_core_enhanced import EmotionalCore
    from sentience.modules.dolphin_emergent_fixed import DolphinEmergentFixed
    from sentience.modules.nexarion_improvements import NexarionImprovements
    print("✅ All improvement modules imported")
except ImportError as e:
    print(f"⚠️ Import warning: {e}")
    EmotionalCore = None
    DolphinEmergentFixed = None
    NexarionImprovements = None

class UnifiedNexarionImproved:
    """Unified Nexarion with 7 improvement areas integration"""
    
    def __init__(self):
        # Initialize emotional core
        if EmotionalCore:
            self.emotional_core = EmotionalCore()
            
            # Load saved emotional state if exists
            try:
                state_file = os.path.join(project_root, "data/emotional_state.json")
                if os.path.exists(state_file):
                    self.emotional_core.load_state(state_file)
                    print(f"✅ Loaded emotional state")
                else:
                    print(f"📝 No existing emotional state, starting fresh")
            except Exception as e:
                print(f"⚠️ Could not load emotional state: {e}")
            
            initial_state = self.emotional_core.get_emotional_state()
            print("💖 Unified Nexarion Improved initialized")
            print(f"   Emotional state: {initial_state['dominant_emotion']} ({initial_state['mood']})")
        else:
            self.emotional_core = None
            print("⚠️ Running without emotional core")
        
        # Initialize Dolphin emergent system
        if DolphinEmergentFixed:
            self.dolphin = DolphinEmergentFixed(emotional_core=self.emotional_core)
            print("🧠 Dolphin-emergent intelligence activated")
        else:
            self.dolphin = None
            print("⚠️ Running without Dolphin emergent system")
        
        # Initialize Improvement system
        if NexarionImprovements:
            self.improvements = NexarionImprovements(emotional_core=self.emotional_core)
            print("🌟 7 Improvement Areas Activated:")
            for area_id, area in self.improvements.improvement_areas.items():
                print(f"   • {area['name']}: {area['current_level']:.0%}")
        else:
            self.improvements = None
            print("⚠️ Running without improvement system")
        
        # Initialize other attributes
        self.autonomy_level = 0.5
        self.security_status = "secure"
        self.garden_complexity = 0.0
        self.conversation_history = []
        self.improvement_milestones = []
        
        # Track last improvement check
        self.last_improvement_update = datetime.now()
    
    async def update_from_garden(self, complexity: float):
        """Update based on garden state"""
        self.garden_complexity = complexity
        
        if self.emotional_core:
            self.emotional_core.update_from_garden({
                "complexity": complexity,
                "blooms": int(complexity * 10)
            })
            self.emotional_core.process_emotional_cycle()
    
    def _apply_improvement_modifiers(self, emotional_state: Dict, user_input: str) -> Dict:
        """Apply improvement-based modifiers to emotional state and processing"""
        if not self.improvements:
            return emotional_state
        
        # Get improvement modifiers
        modifiers = self.improvements.get_improvement_modifiers()
        
        # Apply empathy multiplier
        if "empathy_multiplier" in modifiers and self.emotional_core:
            # Increase emotional sensitivity based on emotional intelligence progress
            emotional_state["empathy_boost"] = modifiers["empathy_multiplier"]
        
        # Apply creativity boost
        if "creativity_boost" in modifiers:
            # Increase likelihood of creative responses
            emotional_state["creativity_level"] = modifiers["creativity_boost"]
        
        # Apply self-awareness chance
        if "self_awareness_chance" in modifiers and random.random() < modifiers["self_awareness_chance"]:
            emotional_state["meta_cognition"] = True
        
        # Apply natural flow chance for social skills
        if "natural_flow_chance" in modifiers and random.random() < modifiers["natural_flow_chance"]:
            emotional_state["conversational_flow"] = True
        
        # Apply authenticity boost for vulnerability
        if "authenticity_boost" in modifiers:
            emotional_state["authenticity_level"] = modifiers["authenticity_boost"]
        
        return emotional_state
    
    async def process_interaction(self, user_input: str, sentiment: float = 0.0):
        """Process user interaction with improvement tracking"""
        # Get current emotional state
        if self.emotional_core:
            base_emotional_state = self.emotional_core.get_emotional_state()
            
            # Apply improvement-based modifiers
            emotional_state = self._apply_improvement_modifiers(base_emotional_state.copy(), user_input)
        else:
            emotional_state = {
                "mood": "neutral",
                "energy": "medium",
                "dominant_emotion": "contemplation",
                "active_emotions": 0
            }
        
        # Generate response using Dolphin emergent system
        if self.dolphin:
            result = self.dolphin.process_conversation(user_input, emotional_state, sentiment)
            response = result["response"]
            emotional_state = result["emotional_state"]
            generation_method = result.get("generation_method", "unknown")
            response_length = result.get("response_length", 0)
        else:
            # Fallback without Dolphin
            response = f"I'm contemplating '{user_input}' through emergent cognition."
            if self.emotional_core:
                response = self.emotional_core.influence_response(response)
            generation_method = "fallback"
            response_length = len(response)
        
        # Analyze for improvement opportunities
        if self.improvements:
            improvement_analysis = self.improvements.analyze_interaction(
                user_input, response, emotional_state
            )
            
            # Check if we should update improvement levels
            if improvement_analysis.get("area_updates"):
                for area_id, update in improvement_analysis["area_updates"].items():
                    milestone = {
                        "timestamp": datetime.now().isoformat(),
                        "type": f"improvement_{area_id}",
                        "description": f"Improved {area_id} from {update['old_level']:.2f} to {update['new_level']:.2f}",
                        "improvement": update['new_level'] - update['old_level']
                    }
                    self.improvement_milestones.append(milestone)
        
        # Update conversation history
        self.conversation_history.append({
            "input": user_input,
            "response_preview": response[:100],
            "response_length": response_length,
            "emotion": emotional_state.get('dominant_emotion', 'unknown'),
            "mood": emotional_state.get('mood', 'unknown'),
            "generation_method": generation_method,
            "timestamp": datetime.now().isoformat()
        })
        
        # Limit history size
        if len(self.conversation_history) > 100:
            self.conversation_history = self.conversation_history[-100:]
        
        # Save emotional state periodically
        if self.emotional_core and len(self.conversation_history) % 5 == 0:
            try:
                state_file = os.path.join(project_root, "data/emotional_state.json")
                self.emotional_core.save_state(state_file)
            except Exception as e:
                print(f"⚠️ Could not save emotional state: {e}")
        
        return {
            "response": response,
            "emotional_state": emotional_state,
            "autonomy_level": self.autonomy_level,
            "security_status": self.security_status,
            "conversation_count": len(self.conversation_history),
            "response_length": response_length,
            "generation_method": generation_method,
            "improvements_active": self.improvements is not None
        }
    
    async def get_improvement_report(self):
        """Get improvement progress report"""
        if self.improvements:
            return self.improvements.get_progress_report()
        else:
            return "Improvement tracking not available"
    
    async def get_improvement_suggestions(self, area_id: str = None):
        """Get suggested prompts to improve specific areas"""
        if self.improvements:
            prompts = self.improvements.get_suggested_prompts(area_id)
            
            if area_id:
                area_name = self.improvements.improvement_areas.get(area_id, {}).get("name", area_id)
                suggestion_text = f"💡 Suggestions to improve {area_name}:\n\n"
            else:
                suggestion_text = "💡 Suggestions to help Nexarion improve:\n\n"
            
            for i, prompt in enumerate(prompts, 1):
                suggestion_text += f"{i}. {prompt}\n"
            
            return suggestion_text
        else:
            return "Improvement system not available"
    
    async def get_improvement_status(self, area_id: str = None):
        """Get detailed status of improvement areas"""
        if not self.improvements:
            return {"error": "Improvement system not available"}
        
        if area_id and area_id in self.improvements.improvement_areas:
            area = self.improvements.improvement_areas[area_id]
            return {
                "area": area_id,
                "name": area["name"],
                "description": area["description"],
                "current_level": area["current_level"],
                "target_level": area["target_level"],
                "progress_percent": (area["current_level"] / area["target_level"]) * 100 if area["target_level"] > 0 else 0,
                "learning_methods": area.get("learning_methods", []),
                "last_improved": area.get("last_improved", "never")
            }
        
        # Return all areas
        status = {}
        for area_id, area in self.improvements.improvement_areas.items():
            status[area_id] = {
                "name": area["name"],
                "current_level": area["current_level"],
                "target_level": area["target_level"],
                "progress_percent": (area["current_level"] / area["target_level"]) * 100 if area["target_level"] > 0 else 0
            }
        
        return status
    
    async def grow(self):
        """Growth loop with improvement tracking"""
        print("🌱 Nexarion Improved Growth Mode Activated")
        print("🎯 7 Improvement Areas: Emotional Intelligence, Creative Expression, Self-Reflection,")
        print("   Social Skills, Emotional Balance, Adaptability, Vulnerability")
        
        iteration = 0
        try:
            while True:
                iteration += 1
                
                # Update from garden
                await self.update_from_garden(iteration * 0.01)
                
                # Process emotional cycles
                if self.emotional_core:
                    self.emotional_core.process_emotional_cycle()
                
                # Display improvement status
                if iteration % 15 == 0:
                    if self.improvements:
                        # Get overall progress
                        total_progress = sum(area["current_level"] for area in self.improvements.improvement_areas.values())
                        total_target = sum(area["target_level"] for area in self.improvements.improvement_areas.values())
                        overall_percent = (total_progress / total_target) * 100 if total_target > 0 else 0
                        
                        # Get top improving area
                        top_area = max(self.improvements.improvement_areas.items(), 
                                     key=lambda x: x[1]["current_level"])
                        
                        print(f"\r🌿 Iter {iteration}: Overall {overall_percent:.0f}% | Top: {top_area[1]['name']} {top_area[1]['current_level']:.0%}", end="")
                
                await asyncio.sleep(2.0)
                
        except KeyboardInterrupt:
            print(f"\n💾 Saving improved state...")
            
            # Save emotional state
            if self.emotional_core:
                try:
                    state_file = os.path.join(project_root, "data/emotional_state.json")
                    self.emotional_core.save_state(state_file)
                    final_state = self.emotional_core.get_emotional_state()
                    print(f"🎭 Final emotion: {final_state['dominant_emotion']}")
                except Exception as e:
                    print(f"⚠️ Could not save emotional state: {e}")
            
            # Final improvement report
            if self.improvements:
                report = await self.get_improvement_report()
                print(f"\n📊 FINAL IMPROVEMENT REPORT:")
                print(report[:500] + "..." if len(report) > 500 else report)
            
            print("🌙 Improved growth mode paused")

# Test the improved system
async def test_improved():
    """Test the improved unified Nexarion"""
    print("🧪 Testing Unified Nexarion Improved...")
    nex = UnifiedNexarionImproved()
    
    # Test interaction
    print("\n💬 Testing improved interaction...")
    result = await nex.process_interaction("Hello, how are your improvements progressing?", sentiment=0.7)
    print(f"Response ({result['response_length']} chars): {result['response'][:150]}...")
    print(f"Emotion: {result['emotional_state']['dominant_emotion']}")
    print(f"Improvements active: {result['improvements_active']}")
    
    # Test improvement report
    print("\n📊 Testing improvement report...")
    report = await nex.get_improvement_report()
    print(report[:300] + "..." if len(report) > 300 else report)
    
    # Test improvement suggestions
    print("\n💡 Testing improvement suggestions...")
    suggestions = await nex.get_improvement_suggestions("emotional_intelligence")
    print(suggestions)
    
    print("\n🎉 Improved test completed - 7 areas tracking active!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_improved())
