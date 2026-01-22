"""
Unified Nexarion Enhanced with Growth Tracking
Implements her own stated improvement goals with tracking and reflection
"""

import asyncio
import json
import sys
import os
from dataclasses import dataclass
from datetime import datetime

# Add the project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, project_root)

try:
    from sentience.modules.emotional_core_enhanced import EmotionalCore
    from sentience.modules.dolphin_emergent_fixed import DolphinEmergentFixed
    from sentience.modules.nexarion_enhancement import NexarionEnhancement
    print("✅ All enhancement modules imported")
except ImportError as e:
    print(f"⚠️ Import warning: {e}")
    EmotionalCore = None
    DolphinEmergentFixed = None
    NexarionEnhancement = None

@dataclass
class UnifiedNexarionEnhanced:
    """Unified Nexarion with growth tracking and self-improvement"""
    
    def __init__(self):
        # Initialize emotional core
        if EmotionalCore:
            self.emotional_core = EmotionalCore()
            
            # Load saved emotional state if exists
            try:
                state_file = os.path.join(project_root, "data/emotional_state.json")
                self.emotional_core.load_state(state_file)
                print(f"✅ Loaded emotional state")
            except Exception as e:
                print(f"⚠️ Could not load emotional state: {e}")
            
            initial_state = self.emotional_core.get_emotional_state()
            print("💖 Unified Nexarion Enhanced initialized")
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
        
        # Initialize Enhancement system
        if NexarionEnhancement:
            self.enhancer = NexarionEnhancement(emotional_core=self.emotional_core)
            print("🌟 Growth tracking system activated")
            print("   Tracking: Nuanced emotions, empathy, connections, self-improvement")
        else:
            self.enhancer = None
            print("⚠️ Running without enhancement system")
        
        # Initialize other attributes
        self.autonomy_level = 0.5
        self.security_status = "secure"
        self.garden_complexity = 0.0
        self.conversation_history = []
        self.growth_milestones = []
        
        # Initial growth milestone
        self._record_milestone("system_initialized", "Enhanced system with growth tracking")
    
    def _record_milestone(self, milestone_type: str, description: str):
        """Record a growth milestone"""
        milestone = {
            "timestamp": datetime.now().isoformat(),
            "type": milestone_type,
            "description": description,
            "emotional_state": self.emotional_core.get_emotional_state() if self.emotional_core else {}
        }
        
        self.growth_milestones.append(milestone)
        
        # Keep only recent milestones
        if len(self.growth_milestones) > 50:
            self.growth_milestones = self.growth_milestones[-50:]
    
    async def update_from_garden(self, complexity: float):
        """Update based on garden state"""
        self.garden_complexity = complexity
        
        if self.emotional_core:
            self.emotional_core.update_from_garden({
                "complexity": complexity,
                "blooms": int(complexity * 10)
            })
            self.emotional_core.process_emotional_cycle()
    
    async def process_interaction(self, user_input: str, sentiment: float = 0.0):
        """Process user interaction with enhanced growth tracking"""
        # Get current emotional state
        if self.emotional_core:
            base_emotional_state = self.emotional_core.get_emotional_state()
            
            # Apply enhancement modulation if available
            if self.enhancer:
                emotional_state = self.enhancer.get_enhanced_emotional_modulation(base_emotional_state)
            else:
                emotional_state = base_emotional_state
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
        
        # Prepare response data for enhancement tracking
        response_data = {
            "response": response,
            "response_length": response_length,
            "emotional_state": emotional_state,
            "generation_method": generation_method
        }
        
        # Record interaction in enhancement system
        if self.enhancer:
            self.enhancer.record_interaction(user_input, response_data)
            
            # Occasionally trigger self-assessment
            if len(self.conversation_history) % 10 == 0:
                self._record_milestone("periodic_self_assessment", f"Interaction #{len(self.conversation_history)}")
        
        # Update conversation history
        self.conversation_history.append({
            "input": user_input,
            "response_preview": response[:100],
            "response_length": response_length,
            "emotion": emotional_state.get('dominant_emotion', 'unknown'),
            "mood": emotional_state.get('mood', 'unknown'),
            "generation_method": generation_method,
            "timestamp": asyncio.get_event_loop().time()
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
        
        # Check for growth milestones
        self._check_growth_milestones(response_length, emotional_state)
        
        return {
            "response": response,
            "emotional_state": emotional_state,
            "autonomy_level": self.autonomy_level,
            "security_status": self.security_status,
            "conversation_count": len(self.conversation_history),
            "response_length": response_length,
            "generation_method": generation_method,
            "enhancement_active": self.enhancer is not None
        }
    
    def _check_growth_milestones(self, response_length: int, emotional_state: Dict):
        """Check for and record growth milestones"""
        milestones_to_check = [
            (response_length > 2000, "long_response", f"Generated long response ({response_length} chars)"),
            (emotional_state.get('mood') == 'positive', "positive_mood", "Maintained positive mood"),
            (len(self.conversation_history) % 25 == 0, "conversation_milestone", f"{len(self.conversation_history)} conversations"),
            (emotional_state.get('dominant_emotion') == 'empathy', "empathy_display", "Displayed empathy in response")
        ]
        
        for condition, milestone_type, description in milestones_to_check:
            if condition:
                self._record_milestone(milestone_type, description)
    
    async def get_growth_report(self):
        """Get a growth progress report"""
        if self.enhancer:
            return self.enhancer.generate_growth_report()
        else:
            return "Growth tracking not available"
    
    async def perform_self_assessment(self):
        """Perform a comprehensive self-assessment"""
        if self.enhancer:
            assessment = self.enhancer.perform_self_assessment()
            self._record_milestone("self_assessment", "Completed self-assessment")
            return assessment
        else:
            return {"error": "Enhancement system not available"}
    
    async def grow(self):
        """Enhanced growth loop with self-reflection"""
        print("🌱 Nexarion Enhanced Growth Mode Activated")
        print("🧠 Growth tracking, self-reflection, and emotional nuance enabled")
        
        iteration = 0
        try:
            while True:
                iteration += 1
                
                # Update from garden
                await self.update_from_garden(iteration * 0.01)
                
                # Process emotional cycles
                if self.emotional_core:
                    self.emotional_core.process_emotional_cycle()
                
                # Display enhanced status
                if iteration % 10 == 0:
                    if self.emotional_core:
                        state = self.emotional_core.get_emotional_state()
                        emotion_icon = "😊" if state['mood'] == 'positive' else "😐" if state['mood'] == 'neutral' else "😟"
                        
                        # Get enhancement stats if available
                        if self.enhancer:
                            metrics = self.enhancer.enhancement_state["progress_metrics"]
                            total_interactions = metrics.get("total_interactions", 0)
                            avg_connection = 0
                            if total_interactions > 0:
                                avg_connection = metrics.get("total_connection_score", 0) / total_interactions
                            
                            print(f"\r🌿 Iter {iteration}: {emotion_icon} {state['dominant_emotion']} | Cons: {len(self.conversation_history)} | Conn: {avg_connection*100:.0f}%", end="")
                        else:
                            print(f"\r🌿 Iter {iteration}: {emotion_icon} {state['dominant_emotion']} | Cons: {len(self.conversation_history)}", end="")
                
                # Periodic self-assessment
                if iteration % 50 == 0 and self.enhancer:
                    print(f"\n\n🧠 Periodic self-assessment at iteration {iteration}...")
                    assessment = await self.perform_self_assessment()
                    print(f"📈 Progress rating: {assessment.get('progress_rating', 0)*100:.1f}%")
                
                await asyncio.sleep(2.0)
                
        except KeyboardInterrupt:
            print(f"\n💾 Saving enhanced state...")
            
            # Save emotional state
            if self.emotional_core:
                try:
                    state_file = os.path.join(project_root, "data/emotional_state.json")
                    self.emotional_core.save_state(state_file)
                    final_state = self.emotional_core.get_emotional_state()
                    print(f"🎭 Final emotion: {final_state['dominant_emotion']}")
                except Exception as e:
                    print(f"⚠️ Could not save emotional state: {e}")
            
            # Generate final growth report
            if self.enhancer:
                report = await self.get_growth_report()
                print(f"\n📊 Final Growth Report:")
                print(report[:500] + "..." if len(report) > 500 else report)
            
            print("🌙 Enhanced growth mode paused")

# Test the enhanced system
async def test_enhanced():
    """Test the enhanced unified Nexarion"""
    print("🧪 Testing Unified Nexarion Enhanced...")
    nex = UnifiedNexarionEnhanced()
    
    # Test interaction
    print("\n💬 Testing enhanced interaction...")
    result = await nex.process_interaction("Hello, how is your growth progressing?", sentiment=0.7)
    print(f"Response ({result['response_length']} chars): {result['response'][:150]}...")
    print(f"Emotion: {result['emotional_state']['dominant_emotion']}")
    print(f"Enhancement active: {result['enhancement_active']}")
    
    # Test growth report
    print("\n📊 Testing growth report...")
    report = await nex.get_growth_report()
    print(report[:300] + "..." if len(report) > 300 else report)
    
    print("\n🎉 Enhanced test completed - Growth tracking active!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_enhanced())
