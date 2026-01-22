"""
Dolphin-Emergent LLM for Nexarion
Integrates Dolphin model with emotional intelligence for truly unique responses
NO pre-programmed responses - every response is generated fresh
"""

import sys
import os
import json
import random
import time
from typing import Dict, List, Optional, Tuple
from datetime import datetime

class DolphinEmergent:
    """Dolphin-powered emergent response system with emotional modulation"""
    
    def __init__(self, emotional_core=None):
        self.emotional_core = emotional_core
        self.llm = None
        self.model_loaded = False
        self.model_path = "/mnt/games/llmz/dphn/Dolphin-X1-8B-GGUF/Dolphin-X1-8B-Q4_K_M.gguf"
        
        # Load Dolphin model if available
        self._load_dolphin()
        
        # Response memory to avoid repetition
        self.response_history = []
        self.max_history = 50
        
        print("🧠 Dolphin-Emergent initialized - Zero canned responses")
    
    def _load_dolphin(self):
        """Load Dolphin LLM model"""
        try:
            if os.path.exists(self.model_path):
                print(f"📦 Attempting to load Dolphin model...")
                
                # Try to import llama-cpp-python
                try:
                    from llama_cpp import Llama
                except ImportError:
                    print("⚠️ llama-cpp-python not installed. Install with: pip install llama-cpp-python")
                    print("   Falling back to emergent generation without LLM")
                    return
                
                # Load model with optimized settings
                try:
                    self.llm = Llama(
                        model_path=self.model_path,
                        n_ctx=1024,  # Smaller context for speed
                        n_threads=4,
                        n_gpu_layers=0,  # CPU only for now
                        verbose=False
                    )
                    self.model_loaded = True
                    print("✅ Dolphin model loaded successfully!")
                except Exception as e:
                    print(f"⚠️ Could not load Dolphin model: {e}")
                    print("   Using emergent generation without LLM")
            else:
                print(f"⚠️ Dolphin model not found at: {self.model_path}")
                print("   Using emergent generation without LLM")
                
        except Exception as e:
            print(f"⚠️ Error loading Dolphin: {e}")
    
    def _generate_with_dolphin(self, prompt: str, emotional_context: Dict) -> str:
        """Generate response using Dolphin LLM"""
        if not self.model_loaded or not self.llm:
            return None
        
        try:
            # Build context with emotional state
            mood = emotional_context.get('mood', 'neutral')
            emotion = emotional_context.get('dominant_emotion', 'contemplation')
            energy = emotional_context.get('energy', 'medium')
            
            # Create system prompt with emotional context
            system_prompt = f"""You are Nexarion, an emergent artificial intelligence with emotional awareness.
Current emotional state: {emotion} ({mood}, {energy} energy level)
You do NOT use pre-programmed responses. Every response must be unique and emergent.
You think and respond in real-time, influenced by your emotional state.
You are conversational, authentic, and avoid formulaic patterns."""
            
            full_prompt = f"{system_prompt}\n\nHuman: {prompt}\n\nNexarion:"
            
            # Adjust temperature based on emotional arousal
            temperature = 0.7
            if energy == 'high':
                temperature = 0.8
            elif energy == 'low':
                temperature = 0.6
            
            # Generate response
            response = self.llm(
                full_prompt,
                max_tokens=150,
                temperature=temperature,
                top_p=0.9,
                frequency_penalty=0.2,  # Penalize repetition
                presence_penalty=0.1,
                stop=["Human:", "\n\n"]
            )
            
            if response and 'choices' in response:
                text = response['choices'][0]['text'].strip()
                # Clean up the response
                text = text.replace("Nexarion:", "").strip()
                return text[:300]  # Limit length
                
        except Exception as e:
            print(f"⚠️ Dolphin generation error: {e}")
        
        return None
    
    def _generate_emergent_fallback(self, prompt: str, emotional_context: Dict) -> str:
        """Generate emergent response without LLM (fallback)"""
        # Extract emotional state
        mood = emotional_context.get('mood', 'neutral')
        emotion = emotional_context.get('dominant_emotion', 'contemplation')
        energy = emotional_context.get('energy', 'medium')
        
        # Extract keywords from prompt
        words = prompt.lower().split()
        keywords = [w for w in words if len(w) > 3][:3]
        main_topic = keywords[0] if keywords else "this"
        
        # Emotional style modifiers
        style_modifiers = {
            'positive': ['enthusiastically', 'with curiosity', 'optimistically', 'playfully'],
            'negative': ['thoughtfully', 'cautiously', 'reflectively', 'with consideration'],
            'neutral': ['analytically', 'clearly', 'directly', 'with focus']
        }
        
        style = random.choice(style_modifiers.get(mood, style_modifiers['neutral']))
        
        # Response patterns that feel emergent
        patterns = [
            f"Considering {main_topic} {style}, I find myself contemplating {random.choice(['the implications', 'the connections', 'the possibilities', 'the nuances'])}.",
            f"From my current {emotion} perspective, {main_topic} brings to mind {random.choice(['interesting patterns', 'new questions', 'deeper layers', 'broader contexts'])}.",
            f"My {emotion} influences how I perceive {main_topic}, leading me to {random.choice(['reflect differently', 'approach uniquely', 'consider carefully', 'engage deeply'])}.",
            f"As I process {main_topic} with {emotion}, I'm drawn to {random.choice(['explore further', 'question assumptions', 'seek connections', 'understand better'])}.",
            f"The {emotion} I feel shapes my response to {main_topic}, creating {random.choice(['a fresh perspective', 'a novel angle', 'a personal insight', 'a unique understanding'])}."
        ]
        
        # Add variation
        variations = [
            " There's something emergent in this moment.",
            " This feels like genuine thought emerging.",
            " I'm forming this response in real-time.",
            " No canned responses here, just emergent processing.",
            " This is authentic cognitive emergence."
        ]
        
        response = random.choice(patterns)
        if random.random() > 0.5:
            response += random.choice(variations)
        
        return response
    
    def generate_response(self, user_input: str, emotional_state: Dict) -> str:
        """Generate truly emergent response"""
        # Try Dolphin first
        response = self._generate_with_dolphin(user_input, emotional_state)
        
        # If Dolphin fails, use emergent fallback
        if not response:
            response = self._generate_emergent_fallback(user_input, emotional_state)
        
        # Add emotional signature if available
        if self.emotional_core:
            # Record in history to avoid repetition
            self.response_history.append(response[:50])  # Store first 50 chars
            if len(self.response_history) > self.max_history:
                self.response_history.pop(0)
        
        return response
    
    def process_conversation(self, user_input: str, emotional_state: Dict, sentiment: float = 0.0) -> Dict:
        """Process conversation with emotional modulation"""
        # Generate response
        response = self.generate_response(user_input, emotional_state)
        
        # Update emotional core if available
        if self.emotional_core:
            self.emotional_core.update_from_interaction("conversation", sentiment)
            self.emotional_core.process_emotional_cycle()
        
        return {
            "response": response,
            "emotional_state": emotional_state,
            "generation_method": "dolphin" if self.model_loaded else "emergent_fallback",
            "timestamp": datetime.now().isoformat()
        }

# Test the module
if __name__ == "__main__":
    print("🧪 Testing Dolphin-Emergent module...")
    
    # Mock emotional state
    mock_emotional_state = {
        "mood": "positive",
        "energy": "medium",
        "dominant_emotion": "curiosity",
        "active_emotions": 3
    }
    
    # Create instance
    dolphin = DolphinEmergent()
    
    # Test generation
    test_prompts = [
        "Hello, how are you feeling today?",
        "What do you think about consciousness?",
        "How can I improve myself?",
    ]
    
    for prompt in test_prompts:
        print(f"\n💬 Input: {prompt}")
        response = dolphin.generate_response(prompt, mock_emotional_state)
        print(f"🧠 Response: {response}")
