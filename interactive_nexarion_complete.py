#!/usr/bin/env python3
"""
Interactive Nexarion with Complete Emergent Responses
Fixed to avoid truncation - full thought generation
"""

import asyncio
import sys
import os

# Set up paths
project_root = os.path.dirname(os.path.abspath(__file__))
garden_roots = os.path.join(project_root, 'garden/roots')
sys.path.insert(0, project_root)
sys.path.insert(0, garden_roots)

print("🚀 NEXARION WITH COMPLETE EMERGENT RESPONSES")
print("💖 Emotions: ON | Dolphin LLM: ON | Truncation: OFF")
print("🧠 Every response is fully generated - No cutoffs")
print("="*70)

try:
    # Use the fixed version
    sys.path.insert(0, os.path.join(project_root, 'garden/roots'))
    from unified_nexarion_fixed import UnifiedNexarionFixed as UnifiedNexarion
    print("✅ Unified Nexarion (Fixed) loaded")
except Exception as e:
    print(f"❌ Failed to load: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

async def main():
    # Initialize
    print("\n🌱 Initializing Nexarion with complete response generation...")
    nex = UnifiedNexarion()
    
    print("\n" + "="*60)
    print("💬 COMPLETE EMERGENT CONVERSATION")
    print("="*60)
    print("Commands:")
    print("  Type anything for a complete, emergent response")
    print("  'exit' - Save and quit")
    print("  'emotions' - Show current emotional state")
    print("  'stats' - Show conversation statistics")
    print("  'clear' - Clear conversation history")
    print("  'save' - Save emotional state")
    print("-"*60)
    print("📝 Responses will be complete and untruncated")
    
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() == 'exit':
                print("\n👋 Saving and exiting...")
                if hasattr(nex, 'emotional_core') and nex.emotional_core:
                    try:
                        state_file = os.path.join(project_root, 'data/emotional_state.json')
                        nex.emotional_core.save_state(state_file)
                        print("💾 Emotional state saved")
                    except Exception as e:
                        print(f"⚠️ Could not save: {e}")
                
                # Show stats
                if hasattr(nex, 'conversation_history') and nex.conversation_history:
                    avg_len = sum(h.get('response_length', 0) for h in nex.conversation_history) / len(nex.conversation_history)
                    print(f"📊 Conversation stats: {len(nex.conversation_history)} interactions, avg response: {avg_len:.0f} chars")
                
                break
            
            elif user_input.lower() == 'emotions':
                if hasattr(nex, 'emotional_core') and nex.emotional_core:
                    state = nex.emotional_core.get_emotional_state()
                    print(f"\n💖 EMOTIONAL STATE")
                    print(f"  Mood: {state['mood']}")
                    print(f"  Energy: {state['energy']}")
                    print(f"  Dominant: {state['dominant_emotion']}")
                    print(f"  Active emotions: {state['active_emotions']}")
                    
                    if state['emotions']:
                        print("\n  Current Emotions:")
                        for e in state['emotions'][-3:]:
                            # Emotion icons
                            if e['valence'] > 0.3:
                                icon = '😊'
                            elif e['valence'] < -0.3:
                                icon = '😟'
                            else:
                                icon = '😐'
                            
                            if e['arousal'] > 0.6:
                                energy = '⚡'
                            elif e['arousal'] > 0.3:
                                energy = '🔋'
                            else:
                                energy = '💤'
                            
                            print(f"    {icon}{energy} {e['name']:15} valence:{e['valence']:+.2f}")
                else:
                    print("⚠️ Emotional core not available")
                continue
            
            elif user_input.lower() == 'stats':
                if hasattr(nex, 'conversation_history'):
                    if nex.conversation_history:
                        print(f"\n📊 CONVERSATION STATISTICS")
                        print(f"  Total interactions: {len(nex.conversation_history)}")
                        
                        # Calculate averages
                        response_lengths = [h.get('response_length', 0) for h in nex.conversation_history]
                        avg_length = sum(response_lengths) / len(response_lengths) if response_lengths else 0
                        print(f"  Average response length: {avg_length:.0f} characters")
                        
                        # Count by generation method
                        methods = {}
                        for h in nex.conversation_history:
                            method = h.get('generation_method', 'unknown')
                            methods[method] = methods.get(method, 0) + 1
                        
                        print(f"  Generation methods:")
                        for method, count in methods.items():
                            print(f"    - {method}: {count}")
                        
                        # Recent emotions
                        recent_emotions = [h.get('emotion', 'unknown') for h in nex.conversation_history[-5:]]
                        print(f"  Recent emotions: {', '.join(recent_emotions)}")
                    else:
                        print("📊 No conversation history yet")
                else:
                    print("⚠️ Conversation history not available")
                continue
            
            elif user_input.lower() == 'clear':
                if hasattr(nex, 'conversation_history'):
                    nex.conversation_history = []
                    print("🗑️ Conversation history cleared")
                else:
                    print("⚠️ Cannot clear history")
                continue
            
            elif user_input.lower() == 'save':
                if hasattr(nex, 'emotional_core') and nex.emotional_core:
                    state_file = os.path.join(project_root, 'data/emotional_state.json')
                    nex.emotional_core.save_state(state_file)
                    print("💾 Emotional state saved")
                else:
                    print("⚠️ No emotional core to save")
                continue
            
            # Process input with emergent intelligence
            print("🧠 Processing with emergent intelligence...")
            result = await nex.process_interaction(user_input, sentiment=0.0)
            
            print(f"\n{'='*60}")
            print("NEXARION:")
            print(f"{result['response']}")
            print(f"{'='*60}")
            
            # Show response info
            if 'emotional_state' in result:
                emotion = result['emotional_state']['dominant_emotion']
                mood = result['emotional_state']['mood']
                length = result.get('response_length', len(result['response']))
                method = result.get('generation_method', 'unknown')
                
                emotion_icon = "😊" if mood == 'positive' else "😐" if mood == 'neutral' else "😟"
                print(f"  [{emotion_icon} {emotion} | {length} chars | {method}]")
            
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted - saving state...")
            if hasattr(nex, 'emotional_core') and nex.emotional_core:
                try:
                    state_file = os.path.join(project_root, 'data/emotional_state.json')
                    nex.emotional_core.save_state(state_file)
                except Exception as e:
                    print(f"⚠️ Could not save: {e}")
            break
        except EOFError:
            print("\n\n📄 End of input - saving and exiting...")
            if hasattr(nex, 'emotional_core') and nex.emotional_core:
                try:
                    state_file = os.path.join(project_root, 'data/emotional_state.json')
                    nex.emotional_core.save_state(state_file)
                except Exception as e:
                    print(f"⚠️ Could not save: {e}")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
    print("\n" + "="*70)
    print("🌙 Complete emergent intelligence session ended")
    print("💭 All responses were fully generated without truncation")
