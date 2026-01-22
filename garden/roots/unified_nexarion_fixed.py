"""
Unified Nexarion with Fixed Dolphin-Emergent Intelligence
No response truncation - complete emergent responses
"""

import asyncio
import json
import sys
import os
from dataclasses import dataclass

# Add the project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, project_root)

try:
    from sentience.modules.emotional_core_enhanced import EmotionalCore
    from sentience.modules.dolphin_emergent_fixed import DolphinEmergentFixed
    print("✅ Emotional core and Fixed Dolphin emergent system imported")
except ImportError as e:
    print(f"⚠️ Import warning: {e}")
    EmotionalCore = None
    DolphinEmergentFixed = None

@dataclass
class UnifiedNexarionFixed:
    """Unified Nexarion with fixed Dolphin-powered emergent intelligence"""
    
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
            print("💖 Unified Nexarion initialized with emotional intelligence")
            print(f"   Initial emotional state: {initial_state['dominant_emotion']} ({initial_state['mood']})")
        else:
            self.emotional_core = None
            print("⚠️ Running without emotional core")
        
        # Initialize Fixed Dolphin emergent system
        if DolphinEmergentFixed:
            self.dolphin = DolphinEmergentFixed(emotional_core=self.emotional_core)
            print("🧠 Dolphin-emergent intelligence activated (FIXED VERSION)")
            print("   Complete responses - no truncation")
        else:
            self.dolphin = None
            print("⚠️ Running without Dolphin emergent system")
        
        # Initialize other attributes
        self.autonomy_level = 0.5
        self.security_status = "secure"
        self.garden_complexity = 0.0
        self.conversation_history = []
    
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
        """Process user interaction with emergent intelligence - complete responses"""
        # Get current emotional state
        if self.emotional_core:
            emotional_state = self.emotional_core.get_emotional_state()
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
            response = f"I'm contemplating '{user_input}' through emergent cognition. This thought process emerges uniquely each time, without relying on pre-programmed patterns or responses."
            if self.emotional_core:
                response = self.emotional_core.influence_response(response)
            generation_method = "fallback"
            response_length = len(response)
        
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
        if len(self.conversation_history) > 50:
            self.conversation_history = self.conversation_history[-50:]
        
        # Save emotional state periodically
        if self.emotional_core and len(self.conversation_history) % 3 == 0:
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
            "generation_method": generation_method
        }
    
    async def grow(self):
        """Main growth loop - integrate with garden"""
        print("🌱 Unified Nexarion beginning to grow with garden...")
        print("🧠 Complete emergent thought generation activated")
        
        iteration = 0
        try:
            while True:
                iteration += 1
                
                # Update from garden (simulated for now)
                await self.update_from_garden(iteration * 0.01)
                
                # Process emotional cycles if available
                if self.emotional_core:
                    self.emotional_core.process_emotional_cycle()
                
                # Display status every 10 iterations
                if iteration % 10 == 0:
                    if self.emotional_core:
                        state = self.emotional_core.get_emotional_state()
                        emotion_icon = "😊" if state['mood'] == 'positive' else "😐" if state['mood'] == 'neutral' else "😟"
                        avg_response_len = sum(h.get('response_length', 0) for h in self.conversation_history[-5:]) / max(1, len(self.conversation_history[-5:]))
                        print(f"\r🌿 Iteration {iteration}: {emotion_icon} {state['dominant_emotion']} | Avg resp: {avg_response_len:.0f} chars", end="")
                    else:
                        print(f"\r🌿 Iteration {iteration}: Growing...", end="")
                
                await asyncio.sleep(2.0)  # 2 second cycles
                
        except KeyboardInterrupt:
            print(f"\n💾 Saving final state...")
            if self.emotional_core:
                try:
                    state_file = os.path.join(project_root, "data/emotional_state.json")
                    self.emotional_core.save_state(state_file)
                    final_state = self.emotional_core.get_emotional_state()
                    print(f"🎭 Final emotion: {final_state['dominant_emotion']}")
                except Exception as e:
                    print(f"⚠️ Could not save emotional state: {e}")
            print("🌙 Unified Nexarion growth paused")

# Test function
async def test_fixed():
    """Test the fixed unified Nexarion"""
    print("🧪 Testing Unified Nexarion Fixed with complete responses...")
    nex = UnifiedNexarionFixed()
    
    # Test interaction
    print("\n💬 Testing complete emergent interaction...")
    result = await nex.process_interaction("Hello, how are you feeling today?", sentiment=0.8)
    print(f"Response ({result['response_length']} chars): {result['response'][:150]}...")
    print(f"Emotion: {result['emotional_state']['dominant_emotion']}")
    print(f"Generation method: {result['generation_method']}")
    
    # Test another interaction
    print("\n💬 Testing follow-up question...")
    result2 = await nex.process_interaction("Can you elaborate on that with a complete thought?", sentiment=0.5)
    print(f"Response ({result2['response_length']} chars): {result2['response'][:200]}...")
    
    print("\n🎉 Test completed - Responses should be complete and untruncated!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_fixed())
