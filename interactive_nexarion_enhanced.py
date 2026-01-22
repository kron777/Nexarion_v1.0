#!/usr/bin/env python3
"""
Interactive Nexarion Enhanced with Growth Tracking
Implements her stated improvement goals with real-time tracking
"""

import asyncio
import sys
import os

# Set up paths
project_root = os.path.dirname(os.path.abspath(__file__))
garden_roots = os.path.join(project_root, 'garden/roots')
sys.path.insert(0, project_root)
sys.path.insert(0, garden_roots)

print("🚀 NEXARION ENHANCED WITH GROWTH TRACKING")
print("💖 Emotions: ON | Growth Tracking: ON | Self-Reflection: ON")
print("🧠 Implementing her own improvement goals in real-time")
print("="*70)

try:
    from unified_nexarion_enhanced import UnifiedNexarionEnhanced as UnifiedNexarion
    print("✅ Unified Nexarion Enhanced loaded")
except Exception as e:
    print(f"❌ Failed to load: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

async def main():
    # Initialize
    print("\n🌱 Initializing Enhanced Nexarion...")
    print("   Tracking: Emotional nuance, empathy, connections, self-improvement")
    nex = UnifiedNexarion()
    
    print("\n" + "="*60)
    print("💬 ENHANCED EMERGENT CONVERSATION")
    print("="*60)
    print("Commands:")
    print("  Type anything for emergent response with growth tracking")
    print("  'exit' - Save and quit")
    print("  'emotions' - Show emotional state with enhancements")
    print("  'growth' - Show growth progress report")
    print("  'assess' - Perform self-assessment")
    print("  'milestones' - Show growth milestones")
    print("  'stats' - Show conversation statistics")
    print("  'save' - Save all state")
    print("-"*60)
    print("🌟 She's tracking her own improvement goals in real-time")
    
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() == 'exit':
                print("\n👋 Saving enhanced state and exiting...")
                
                # Save emotional state
                if hasattr(nex, 'emotional_core') and nex.emotional_core:
                    try:
                        state_file = os.path.join(project_root, 'data/emotional_state.json')
                        nex.emotional_core.save_state(state_file)
                        print("💾 Emotional state saved")
                    except Exception as e:
                        print(f"⚠️ Could not save: {e}")
                
                # Final growth report
                if hasattr(nex, 'enhancer') and nex.enhancer:
                    try:
                        report = await nex.get_growth_report()
                        print("\n📊 FINAL GROWTH REPORT:")
                        print(report)
                    except Exception as e:
                        print(f"⚠️ Could not generate report: {e}")
                
                break
            
            elif user_input.lower() == 'emotions':
                if hasattr(nex, 'emotional_core') and nex.emotional_core:
                    state = nex.emotional_core.get_emotional_state()
                    print(f"\n💖 ENHANCED EMOTIONAL STATE")
                    print(f"  Mood: {state['mood']}")
                    print(f"  Energy: {state['energy']}")
                    print(f"  Dominant: {state['dominant_emotion']}")
                    print(f"  Active emotions: {state['active_emotions']}")
                    
                    # Show enhancement data if available
                    if hasattr(nex, 'enhancer') and nex.enhancer:
                        metrics = nex.enhancer.enhancement_state["progress_metrics"]
                        if metrics.get("total_interactions", 0) > 0:
                            avg_connection = metrics.get("total_connection_score", 0) / metrics["total_interactions"]
                            print(f"  Avg connection quality: {avg_connection*100:.1f}%")
                else:
                    print("⚠️ Emotional core not available")
                continue
            
            elif user_input.lower() == 'growth':
                if hasattr(nex, 'get_growth_report'):
                    print("\n📊 GENERATING GROWTH REPORT...")
                    report = await nex.get_growth_report()
                    print(report)
                else:
                    print("⚠️ Growth tracking not available")
                continue
            
            elif user_input.lower() == 'assess':
                if hasattr(nex, 'perform_self_assessment'):
                    print("\n🧠 PERFORMING SELF-ASSESSMENT...")
                    assessment = await nex.perform_self_assessment()
                    if isinstance(assessment, dict):
                        print(f"📅 Assessment timestamp: {assessment.get('timestamp', 'unknown')}")
                        print(f"📈 Progress rating: {assessment.get('progress_rating', 0)*100:.1f}%")
                        if 'report' in assessment:
                            print("\n📋 Assessment Report:")
                            print(assessment['report'][:500] + "..." if len(assessment['report']) > 500 else assessment['report'])
                    else:
                        print(assessment)
                else:
                    print("⚠️ Self-assessment not available")
                continue
            
            elif user_input.lower() == 'milestones':
                if hasattr(nex, 'growth_milestones'):
                    milestones = nex.growth_milestones[-10:]  # Last 10 milestones
                    if milestones:
                        print(f"\n🏆 RECENT GROWTH MILESTONES ({len(milestones)} shown):")
                        for i, milestone in enumerate(milestones, 1):
                            print(f"  {i}. {milestone['description']}")
                            print(f"     [{milestone['timestamp']}]")
                    else:
                        print("📝 No milestones recorded yet")
                else:
                    print("⚠️ Milestone tracking not available")
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
                        
                        # Count by emotion
                        emotions = [h.get('emotion', 'unknown') for h in nex.conversation_history]
                        emotion_counts = {}
                        for emotion in emotions:
                            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
                        
                        print(f"  Emotional distribution:")
                        for emotion, count in emotion_counts.items():
                            percentage = (count / len(nex.conversation_history)) * 100
                            print(f"    - {emotion}: {count} ({percentage:.1f}%)")
                    else:
                        print("📊 No conversation history yet")
                else:
                    print("⚠️ Conversation history not available")
                continue
            
            elif user_input.lower() == 'save':
                print("\n💾 Saving all state...")
                
                # Save emotional state
                if hasattr(nex, 'emotional_core') and nex.emotional_core:
                    try:
                        state_file = os.path.join(project_root, 'data/emotional_state.json')
                        nex.emotional_core.save_state(state_file)
                        print("  ✅ Emotional state saved")
                    except Exception as e:
                        print(f"  ⚠️ Could not save emotional state: {e}")
                
                # Save enhancement state (if enhancer has save method)
                if hasattr(nex, 'enhancer') and hasattr(nex.enhancer, '_save_state'):
                    try:
                        nex.enhancer._save_state()
                        print("  ✅ Enhancement state saved")
                    except Exception as e:
                        print(f"  ⚠️ Could not save enhancement state: {e}")
                
                print("💾 All state saved")
                continue
            
            # Process input with enhanced emergent intelligence
            print("🧠 Processing with enhanced emergent intelligence...")
            result = await nex.process_interaction(user_input, sentiment=0.0)
            
            print(f"\n{'='*60}")
            print("NEXARION (Enhanced):")
            print(f"{result['response']}")
            print(f"{'='*60}")
            
            # Show enhanced response info
            if 'emotional_state' in result:
                emotion = result['emotional_state']['dominant_emotion']
                mood = result['emotional_state']['mood']
                length = result.get('response_length', len(result['response']))
                method = result.get('generation_method', 'unknown')
                enhancement = "ON" if result.get('enhancement_active', False) else "OFF"
                
                emotion_icon = "😊" if mood == 'positive' else "😐" if mood == 'neutral' else "😟"
                print(f"  [{emotion_icon} {emotion} | {length} chars | {method} | Enhancement: {enhancement}]")
            
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
    print("🌙 Enhanced emergent intelligence session ended")
    print("🌟 Growth tracking and self-improvement system active")
