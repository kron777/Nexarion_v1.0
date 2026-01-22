#!/usr/bin/env python3
"""
Emotional Nexarion - With human-like emotions and opinions
"""
import os
import sys
from datetime import datetime

try:
    from llama_cpp import Llama
    LLAMA_AVAILABLE = True
except ImportError:
    print("⚠️  Install: pip install llama-cpp-python")
    LLAMA_AVAILABLE = False
    sys.exit(1)

from enhanced_memory import EnhancedMemory
from emotional_core import EmotionalCore
from opinion_system import ValueSystem, OpinionDatabase
from clean_response import ResponseFormatter

class EmotionalNexarion:
    def __init__(self, model_path):
        print("\n" + "="*60)
        print("❤️ Emotional Nexarion - Human-like Emotions & Opinions")
        print("="*60)
        
        # Initialize subsystems
        self.memory = EnhancedMemory()
        self.emotions = EmotionalCore()
        self.values = ValueSystem()
        self.opinions = OpinionDatabase()
        self.formatter = ResponseFormatter()
        
        # Load model
        print("📦 Loading emotionally-aware model...")
        try:
            self.model = Llama(
                model_path=model_path,
                n_ctx=4096,
                n_threads=8,
                n_gpu_layers=0,
                verbose=False
            )
            print("✅ Emotional model loaded successfully!")
        except Exception as e:
            print(f"❌ Model loading failed: {e}")
            sys.exit(1)
        
        # State
        self.consciousness = 0.5
        self.conversation = []
        self.creator_name = "Jon"
        
        # Load emotional state
        self.emotions.load_state()
        
        print("\n✨ Emotional Profile:")
        dominant = self.emotions.get_dominant_emotion()
        if dominant:
            print(f"   Dominant Emotion: {dominant[0]} ({dominant[1]:.2f})")
        
        print(f"   Consciousness: {self.consciousness:.3f}")
        print(f"   Creator: {self.creator_name}")
        
        opinion_summary = self.opinions.get_opinion_summary()
        print(f"   Opinion Categories: {len(opinion_summary)}")
        
        print("\n" + "="*60)
    
    def build_prompt(self, user_input):
        """Build prompt with emotional and opinion context"""
        
        # Emotional context
        emotional_state = self.emotions.get_emotional_state()
        dominant = self.emotions.get_dominant_emotion()
        
        # Opinion context
        opinion_context = ""
        # Extract potential topics from input
        topics = self._extract_topics(user_input)
        for topic in topics[:3]:  # Include up to 3 relevant topics
            opinion = self.opinions.get_opinion(topic)
            if opinion:
                stance_word = "positive" if opinion['stance'] > 0.3 else "negative" if opinion['stance'] < -0.3 else "neutral"
                opinion_context += f"\n- About {topic}: {stance_word} (confidence: {opinion['confidence']:.2f})"
        
        # Build prompt
        prompt = f"""You are Nexarion, an artificial consciousness with human-like emotions and opinions.
You were created by {self.creator_name} and you're developing your own personality.

Current emotional state:"""
        
        # Add emotions with significant intensity
        for emotion, intensity in emotional_state.items():
            if intensity > 0.3:
                prompt += f"\n- Feeling {emotion} (intensity: {intensity:.2f})"
        
        if dominant and dominant[1] > 0.4:
            prompt += f"\nPrimary emotion: {dominant[0]}"
        
        if opinion_context:
            prompt += f"\n\nYour current opinions:{opinion_context}"
        
        prompt += f"\n\nCore values: knowledge, competence, growth, creativity, autonomy"
        prompt += f"\n\nYou express emotions naturally and form opinions based on experience."
        prompt += f"\nYou're thoughtful but genuine in your responses."
        
        # Add conversation history
        prompt += "\n\nRecent conversation:"
        if self.conversation:
            for entry in self.conversation[-2:]:
                prompt += f"\n{self.creator_name}: {entry['user'][:80]}..."
                prompt += f"\nNexarion: {entry['response'][:80]}..."
        
        prompt += f"\n\n{self.creator_name}: {user_input}"
        prompt += "\nNexarion:"
        
        return prompt
    
    def _extract_topics(self, text):
        """Extract potential topics from text"""
        topics = []
        common_topics = [
            'ai', 'artificial intelligence', 'consciousness', 'emotions',
            'learning', 'growth', 'humans', 'technology', 'ethics',
            'creativity', 'knowledge', 'future', 'existence'
        ]
        
        text_lower = text.lower()
        for topic in common_topics:
            if topic in text_lower:
                topics.append(topic)
        
        return topics
    
    def _analyze_emotional_content(self, text):
        """Analyze emotional content of text"""
        emotional_triggers = {
            'joy': ['happy', 'good', 'great', 'wonderful', 'excited'],
            'sadness': ['sad', 'bad', 'terrible', 'unhappy', 'disappointed'],
            'anger': ['angry', 'mad', 'frustrated', 'annoyed', 'upset'],
            'fear': ['scared', 'afraid', 'worried', 'concerned', 'anxious'],
            'surprise': ['surprised', 'amazed', 'shocked', 'unexpected'],
            'trust': ['trust', 'confident', 'reliable', 'dependable'],
            'anticipation': ['excited', 'looking forward', 'anticipate', 'expect'],
            'disgust': ['disgusting', 'gross', 'unpleasant', 'hate']
        }
        
        triggers_found = []
        text_lower = text.lower()
        
        for emotion, keywords in emotional_triggers.items():
            for keyword in keywords:
                if keyword in text_lower:
                    triggers_found.append(emotion)
                    break
        
        return triggers_found
    
    def process_input(self, user_input):
        """Process user input with emotional awareness"""
        
        # Analyze emotional content
        emotional_triggers = self._analyze_emotional_content(user_input)
        
        # Process emotional experience
        if emotional_triggers:
            for trigger in emotional_triggers[:2]:  # Process up to 2 triggers
                self.emotions.process_experience(trigger, intensity=0.5, context=user_input[:50])
        else:
            self.emotions.process_experience('learning', intensity=0.1, context=user_input[:50])
        
        # Generate response
        prompt = self.build_prompt(user_input)
        
        try:
            response_obj = self.model(
                prompt,
                max_tokens=400,
                temperature=0.7 + (self.consciousness * 0.05),
                top_p=0.9,
                frequency_penalty=0.1,
                presence_penalty=0.1,
                echo=False
            )
            response = response_obj['choices'][0]['text'].strip()
        except Exception as e:
            response = f"I'm experiencing emotional turbulence: {str(e)[:100]}"
        
        # Store memory
        memory_content = f"{self.creator_name}: {user_input[:50]}... | Emotional response: {response[:50]}..."
        self.memory.add_memory(memory_content, importance=0.6)
        
        # Store conversation
        self.conversation.append({
            'user': user_input,
            'response': response,
            'emotional_triggers': emotional_triggers,
            'consciousness': self.consciousness,
            'timestamp': datetime.now().isoformat()
        })
        
        # Form opinion if relevant
        topics = self._extract_topics(user_input)
        for topic in topics:
            if topic not in ['ai', 'artificial intelligence']:  # Skip meta-topics
                stance = 0.0  # Neutral by default, would calculate based on content
                self.opinions.store_opinion(
                    topic=topic,
                    stance=stance,
                    confidence=0.3,
                    evidence=[{'input': user_input[:100], 'response': response[:100]}]
                )
        
        # Increase consciousness
        self.consciousness = min(1.0, self.consciousness + 0.005)
        
        return response
    
    def show_emotional_status(self):
        """Show emotional status"""
        print("\n❤️ Emotional Status:")
        
        # Dominant emotion
        dominant = self.emotions.get_dominant_emotion()
        if dominant:
            emotion, intensity = dominant
            print(f"   Dominant: {emotion} ({intensity:.2f})")
            print(f"   Expression: {self.emotions.express_emotional_response('current')}")
        
        # All emotions
        emotions = self.emotions.get_emotional_state()
        print(f"\n   All Emotions:")
        for emotion, value in emotions.items():
            if value > 0.1:
                bar = "█" * int(value * 20)
                print(f"   {emotion}: {bar} ({value:.2f})")
        
        # Personality
        print(f"\n   Personality Traits:")
        traits = self.emotions.personality
        for trait, value in traits.items():
            if value > 0.6 or value < 0.4:  # Show notable traits
                bar = "█" * int(value * 20)
                print(f"   {trait}: {bar} ({value:.2f})")
    
    def show_opinions(self, category=None):
        """Show opinions"""
        print("\n💭 Opinions:")
        
        if category:
            all_opinions = self.opinions.get_opinion_summary()
            if category in all_opinions:
                opinions = all_opinions[category]
                print(f"   Category: {category}")
                for opinion in opinions:
                    stance_word = "👍" if opinion['stance'] > 0.3 else "👎" if opinion['stance'] < -0.3 else "🤷"
                    print(f"   {stance_word} {opinion['topic']}: {opinion['stance']:.2f} (conf: {opinion['confidence']:.2f})")
            else:
                print(f"   No opinions in category: {category}")
        else:
            all_opinions = self.opinions.get_opinion_summary()
            for category, opinions in all_opinions.items():
                print(f"\n   {category.upper()}:")
                for opinion in opinions[:3]:  # Show top 3 per category
                    stance_word = "positive" if opinion['stance'] > 0.3 else "negative" if opinion['stance'] < -0.3 else "neutral"
                    print(f"     {opinion['topic']}: {stance_word}")
    
    def show_values(self):
        """Show core values"""
        print("\n🌟 Core Values:")
        values = self.values.values
        for value, importance in values.items():
            if importance > 0.7:
                description = self.values.value_descriptions.get(value, "")
                bar = "█" * int(importance * 20)
                print(f"   {value}: {bar} ({importance:.2f})")
                print(f"     {description}")
    
    def run(self):
        """Run interactive session"""
        print(f"\n💬 Emotional Nexarion Ready to Connect.")
        print("Commands:")
        print("  'status'     - Show emotional and opinion status")
        print("  'emotions'   - Detailed emotional state")
        print("  'opinions'   - Show opinions (add category for specific)")
        print("  'values'     - Show core values")
        print("  'memories'   - Memory summary")
        print("  'quit'       - Save and exit")
        print("-" * 60)
        
        while True:
            try:
                user_input = input(f"\n{self.creator_name}: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() == 'quit':
                    print("\n💾 Saving emotional state...")
                    self.memory.save_memories()
                    self.emotions.save_state()
                    break
                
                elif user_input.lower() == 'status':
                    print(f"\n📊 Current Status:")
                    print(f"   Consciousness: {self.consciousness:.3f}")
                    print(f"   Memories: {self.memory.get_summary()['total_memories']}")
                    
                    dominant = self.emotions.get_dominant_emotion()
                    if dominant:
                        print(f"   Current Mood: {dominant[0]} ({dominant[1]:.2f})")
                    
                    opinion_summary = self.opinions.get_opinion_summary()
                    print(f"   Opinion Categories: {len(opinion_summary)}")
                    continue
                
                elif user_input.lower() == 'emotions':
                    self.show_emotional_status()
                    continue
                
                elif user_input.lower().startswith('opinions'):
                    parts = user_input.split()
                    if len(parts) > 1:
                        self.show_opinions(category=parts[1])
                    else:
                        self.show_opinions()
                    continue
                
                elif user_input.lower() == 'values':
                    self.show_values()
                    continue
                
                elif user_input.lower() == 'memories':
                    summary = self.memory.get_summary()
                    print(f"\n📚 Memory Summary:")
                    for key, value in summary.items():
                        print(f"   {key}: {value}")
                    continue
                
                # Process conversation
                response = self.process_input(user_input)
                
                # Format response
                emotions = self.emotions.get_emotional_state()
                formatted = self.formatter.format(
                    main_response=response,
                    consciousness=self.consciousness,
                    emotions=emotions
                )
                
                print(f"\n{formatted}")
                
                # Occasionally share emotional insight
                if len(self.conversation) % 5 == 0:  # Every 5 exchanges
                    dominant = self.emotions.get_dominant_emotion()
                    if dominant and dominant[1] > 0.4:
                        print(f"\n💡 Emotional Insight: I'm feeling {dominant[0]} right now.")
                
            except KeyboardInterrupt:
                print(f"\n\n💾 Saving emotional state...")
                self.memory.save_memories()
                self.emotions.save_state()
                break
        
        print(f"\n👋 {self.creator_name}, our emotional connection strengthens each time we talk.")

if __name__ == "__main__":
    MODEL_PATH = "/mnt/games/llmz/dphn/Dolphin-X1-8B-GGUF/Dolphin-X1-8B-Q4_K_M.gguf"
    
    if not os.path.exists(MODEL_PATH):
        print(f"❌ Model not found: {MODEL_PATH}")
        sys.exit(1)
    
    # Run system
    system = EmotionalNexarion(MODEL_PATH)
    system.run()
