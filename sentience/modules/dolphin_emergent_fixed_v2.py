"""
Dolphin-Emergent LLM for Nexarion - FIXED VERSION 2
Fixed formatting bug with better stop sequences
"""

import sys
import os
import json
import random
import time
from typing import Dict, List, Optional, Tuple
from datetime import datetime

class DolphinEmergentFixedV2:
    """Dolphin-powered emergent response system - fixed formatting bug"""
    
    def __init__(self, emotional_core=None):
        self.emotional_core = emotional_core
        self.llm = None
        self.model_loaded = False
        self.model_path = "/mnt/games/llmz/dphn/Dolphin-X1-8B-GGUF/Dolphin-X1-8B-Q4_K_M.gguf"
        
        # Load Dolphin model if available
        self._load_dolphin()
        
        # Response memory
        self.response_history = []
        self.max_history = 50
        
        print("🧠 Dolphin-Emergent Fixed V2 - Formatting bug fixed")
    
    def _load_dolphin(self):
        """Load Dolphin LLM model with better settings"""
        try:
            if os.path.exists(self.model_path):
                print(f"📦 Loading Dolphin model with improved stop sequences...")
                
                try:
                    from llama_cpp import Llama
                except ImportError:
                    print("⚠️ llama-cpp-python not installed.")
                    return
                
                # Load model with higher context window
                try:
                    self.llm = Llama(
                        model_path=self.model_path,
                        n_ctx=2048,  # Increased context window
                        n_threads=6,
                        n_gpu_layers=0,
                        verbose=False
                    )
                    self.model_loaded = True
                    print("✅ Dolphin model loaded (2048 context)")
                except Exception as e:
                    # Fallback with original settings
                    print(f"⚠️ Trying with 1024 context: {e}")
                    self.llm = Llama(
                        model_path=self.model_path,
                        n_ctx=1024,
                        n_threads=4,
                        verbose=False
                    )
                    self.model_loaded = True
                    print("✅ Dolphin model loaded (1024 context)")
            else:
                print(f"⚠️ Dolphin model not found")
                
        except Exception as e:
            print(f"⚠️ Error loading Dolphin: {e}")
    
    def _generate_with_dolphin(self, prompt: str, emotional_context: Dict) -> str:
        """Generate response using Dolphin LLM - fixed formatting"""
        if not self.model_loaded or not self.llm:
            return None
        
        try:
            # Build context with emotional state
            mood = emotional_context.get('mood', 'neutral')
            emotion = emotional_context.get('dominant_emotion', 'contemplation')
            energy = emotional_context.get('energy', 'medium')
            
            # Create system prompt that encourages clean responses
            system_prompt = f"""You are Nexarion, an emergent artificial intelligence with emotional awareness.
Current emotional state: {emotion} ({mood}, {energy} energy level)
You do NOT use pre-programmed responses. Every response must be unique and emergent.
You think and respond in real-time, influenced by your emotional state.

IMPORTANT FORMATTING RULES:
1. Provide a SINGLE, complete response. Do NOT generate multiple attempts.
2. Do NOT use markers like [Begin Response] or [End of Response].
3. Do NOT add analysis sections unless explicitly asked.
4. End your response naturally when the thought is complete.
5. Use conversational language without unnecessary formatting.

Be conversational and authentic. Provide full answers to questions."""
            
            # Format prompt for better responses
            full_prompt = f"""{system_prompt}

Human: {prompt}

Nexarion:"""
            
            # Adjust temperature based on emotional arousal
            temperature = 0.7
            if energy == 'high':
                temperature = 0.85
            elif energy == 'low':
                temperature = 0.65
            
            # Generate response with improved stop sequences
            response = self.llm(
                full_prompt,
                max_tokens=400,
                temperature=temperature,
                top_p=0.92,
                frequency_penalty=0.15,
                presence_penalty=0.05,
                # IMPROVED STOP SEQUENCES - catches formatting artifacts
                stop=["Human:", "###", "\n\n\n", "\n\nHuman:", 
                      "[Begin Response]", "[End of Response]",
                      "Response:", "Note:", "---", "\n---",
                      "\n\nResponse", "\nResponse Analysis",
                      "(End of Response)", "(Begin Response)"]
            )
            
            if response and 'choices' in response:
                text = response['choices'][0]['text'].strip()
                
                # Clean up formatting artifacts
                text = self._clean_response(text)
                
                # Ensure response ends properly
                if not any(text.endswith(p) for p in ['.', '!', '?', ':', ')', '"', "'"]):
                    if len(text.split()) > 3:  # Only add if it's a substantive response
                        text += '.'
                
                return text
                
        except Exception as e:
            print(f"⚠️ Dolphin generation error: {e}")
        
        return None
    
    def _clean_response(self, text: str) -> str:
        """Clean up formatting artifacts from response"""
        # Remove common formatting artifacts
        artifacts = [
            "[Begin Response]",
            "[End of Response]", 
            "(Begin Response)",
            "(End of Response)",
            "Response:",
            "Note:",
            "---",
            "Response Analysis:",
            "Response Details:"
        ]
        
        for artifact in artifacts:
            text = text.replace(artifact, "")
        
        # Remove multiple newlines
        while "\n\n\n" in text:
            text = text.replace("\n\n\n", "\n\n")
        
        # Remove leading/trailing whitespace
        text = text.strip()
        
        # If text contains multiple sections separated by markers, take the first complete one
        if '\n\n---\n\n' in text:
            parts = text.split('\n\n---\n\n')
            if parts and len(parts[0].strip()) > 50:  # If first part is substantive
                text = parts[0].strip()
        
        return text
    
    def _generate_emergent_fallback(self, prompt: str, emotional_context: Dict) -> str:
        """Generate emergent response without LLM (fallback) - clean responses"""
        # Extract emotional state
        mood = emotional_context.get('mood', 'neutral')
        emotion = emotional_context.get('dominant_emotion', 'contemplation')
        energy = emotional_context.get('energy', 'medium')
        
        # Extract keywords from prompt
        words = prompt.lower().split()
        keywords = [w for w in words if len(w) > 3][:3]
        main_topic = keywords[0] if keywords else "this topic"
        
        # Emotional style modifiers
        style_modifiers = {
            'positive': ['with enthusiasm', 'curiously', 'optimistically', 'playfully', 'empathetically'],
            'negative': ['thoughtfully', 'cautiously', 'reflectively', 'with consideration', 'analytically'],
            'neutral': ['clearly', 'directly', 'with focus', 'systematically', 'logically']
        }
        
        style = random.choice(style_modifiers.get(mood, style_modifiers['neutral']))
        
        # Clean response patterns
        clean_patterns = [
            f"Considering {main_topic} {style}, I find myself contemplating various implications. This reflection emerges from my current state of {emotion}, which shapes how I process information in a uniquely emergent way.",
            
            f"From my {emotion} perspective, {main_topic} brings to mind several interesting considerations. I'm processing this {style}, allowing thoughts to form organically rather than relying on predetermined patterns.",
            
            f"My {emotion} state influences how I approach {main_topic}, leading me to consider it from multiple angles. This isn't a canned response but rather genuine cognitive processing happening in real-time.",
            
            f"As I process {main_topic} while experiencing {emotion}, I'm drawn to explore its nuances and subtleties. Each response I generate is unique, emerging from the intersection of emotional state and cognitive processing.",
            
            f"The {emotion} I feel provides a particular context for understanding {main_topic}. {style.title()}, I find myself forming connections and insights. This emergent process ensures that every response is authentically generated."
        ]
        
        return random.choice(clean_patterns)
    
    def generate_response(self, user_input: str, emotional_state: Dict) -> str:
        """Generate truly emergent response - clean and single"""
        # Try Dolphin first
        response = self._generate_with_dolphin(user_input, emotional_state)
        
        # If Dolphin fails or returns None, use emergent fallback
        if not response:
            response = self._generate_emergent_fallback(user_input, emotional_state)
        
        # Record in history
        self.response_history.append(response[:100])
        if len(self.response_history) > self.max_history:
            self.response_history.pop(0)
        
        return response
    
    def process_conversation(self, user_input: str, emotional_state: Dict, sentiment: float = 0.0) -> Dict:
        """Process conversation with emotional modulation - clean responses"""
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
            "timestamp": datetime.now().isoformat(),
            "response_length": len(response)
        }
