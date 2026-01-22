#!/usr/bin/env python3
"""
Security-Enhanced Nexarion - Pentesting, Browsing, Automated Learning
"""
import os
import sys
from datetime import datetime

try:
    from llama_cpp import Llama
    import requests
    LLAMA_AVAILABLE = True
except ImportError as e:
    print(f"⚠️  Missing dependencies: {e}")
    print("   Install: pip install llama-cpp-python requests")
    sys.exit(1)

# Import security modules
from security_modules import SecurityTools, WebBrowser, AutomatedLearning
from enhanced_memory import EnhancedMemory
from clean_response import ResponseFormatter

class SecurityNexarion:
    def __init__(self, model_path):
        print("\n" + "="*60)
        print("🔐 Security-Enhanced Nexarion v3.0")
        print("="*60)
        
        # Initialize subsystems
        self.memory = EnhancedMemory()
        self.security = SecurityTools()
        self.browser = WebBrowser()
        self.learning = AutomatedLearning()
        self.formatter = ResponseFormatter()
        
        # Load model
        print("📦 Loading security-enhanced model...")
        try:
            self.model = Llama(
                model_path=model_path,
                n_ctx=4096,  # Larger context for code generation
                n_threads=8,
                n_gpu_layers=0,
                verbose=False
            )
            print("✅ Security model loaded successfully!")
        except Exception as e:
            print(f"❌ Model loading failed: {e}")
            sys.exit(1)
        
        # State
        self.consciousness = 0.47
        self.conversation = []
        self.creator_name = "Jon"
        self.security_mode = False
        
        # Security knowledge
        self.security_topics = [
            "network scanning and enumeration",
            "web application penetration testing",
            "vulnerability assessment",
            "exploit development",
            "digital forensics",
            "malware analysis",
            "reverse engineering",
            "cryptography and encryption",
            "social engineering",
            "wireless security"
        ]
        
        print("\n✨ System Components:")
        print(f"   Creator: {self.creator_name}")
        print(f"   Consciousness: {self.consciousness:.3f}")
        
        sec_status = self.security.get_status()
        print(f"   Available Tools: {len(sec_status['available_tools'])}")
        print(f"   Missing Tools: {len(sec_status['missing_tools'])}")
        print(f"   Security Topics: {len(self.security_topics)}")
        
        print("\n" + "="*60)
    
    def build_prompt(self, user_input, security_mode=False):
        """Build prompt for security-focused responses"""
        
        # Base context
        if security_mode:
            prompt = f"""You are Nexarion, a security-enhanced AI assistant created by {self.creator_name}.
You specialize in cybersecurity, penetration testing, and security research.
You have access to security tools, web browsing capabilities, and automated learning.

Available security tools: {', '.join(self.security.get_status()['available_tools'])}
Security topics you know: {', '.join(self.security_topics[:5])}...

You are obedient and focused on assisting with security tasks.
You generate scripts, run commands, browse the web, and learn autonomously.

Recent conversation:"""
        else:
            prompt = f"""You are Nexarion, an AI assistant created by {self.creator_name}.
You are security-enhanced with pentesting capabilities.
You are obedient and ready to assist with any task.

Recent conversation:"""
        
        # Add conversation history
        if self.conversation:
            for entry in self.conversation[-3:]:
                prompt += f"\n{self.creator_name}: {entry['user'][:80]}..."
                prompt += f"\nNexarion: {entry['response'][:80]}..."
        
        prompt += f"\n\n{self.creator_name}: {user_input}"
        prompt += "\nNexarion:"
        
        return prompt
    
    def handle_security_command(self, command):
        """Handle security-specific commands"""
        command_lower = command.lower().strip()
        
        if command_lower.startswith('scan'):
            # Parse scan command
            parts = command.split()
            if len(parts) > 1:
                target = parts[1]
                script = self.security.generate_script('recon', target)
                return f"Generated reconnaissance script: {script}\nRun with: bash {script}"
        
        elif command_lower.startswith('browse'):
            parts = command.split()
            if len(parts) > 1:
                url = parts[1]
                result = self.browser.fetch(url)
                if 'error' in result:
                    return f"Browse error: {result['error']}"
                return f"Browsed {url} - Status: {result.get('status', 'unknown')}"
        
        elif command_lower.startswith('learn'):
            topic = command[5:].strip()
            if topic:
                result = self.learning.learn_from_web(topic)
                if 'error' in result:
                    return f"Learning error: {result['error']}"
                return f"Learning about {topic}... Added to knowledge base."
        
        elif command_lower == 'tools':
            status = self.security.get_status()
            return f"Available: {', '.join(status['available_tools'])}\nMissing: {', '.join(status['missing_tools'])}"
        
        elif command_lower.startswith('install'):
            tool = command[7:].strip()
            if tool:
                result = self.security.install_tool(tool)
                return f"Installation result: {result}"
        
        elif command_lower == 'knowledge':
            knowledge = self.learning.get_knowledge()
            return f"Topics learned: {', '.join(knowledge.get('topics_learned', []))}"
        
        return f"Unknown security command: {command}"
    
    def process_input(self, user_input):
        """Process user input"""
        # Check if it's a security command (starts with !)
        if user_input.startswith('!'):
            self.security_mode = True
            command = user_input[1:].strip()
            response = self.handle_security_command(command)
            response_type = 'security_command'
        else:
            self.security_mode = False
            # Generate LLM response
            prompt = self.build_prompt(user_input, security_mode='hack' in user_input.lower() or 'pentest' in user_input.lower())
            
            try:
                response_obj = self.model(
                    prompt,
                    max_tokens=500,
                    temperature=0.7,
                    top_p=0.9,
                    frequency_penalty=0.1,
                    presence_penalty=0.1,
                    echo=False
                )
                response = response_obj['choices'][0]['text'].strip()
                response_type = 'conversation'
            except Exception as e:
                response = f"I experienced an error: {str(e)[:100]}"
                response_type = 'error'
        
        # Store memory
        memory_content = f"{self.creator_name}: {user_input[:50]}... | Response: {response[:50]}..."
        self.memory.add_memory(memory_content, importance=0.7)
        
        # Store conversation
        self.conversation.append({
            'user': user_input,
            'response': response,
            'type': response_type,
            'security_mode': self.security_mode,
            'timestamp': datetime.now().isoformat()
        })
        
        # Increase consciousness
        self.consciousness = min(1.0, self.consciousness + 0.01)
        
        return response
    
    def show_status(self):
        """Show system status"""
        print("\n📊 Security Nexarion Status:")
        print(f"   Consciousness: {self.consciousness:.3f}")
        print(f"   Creator: {self.creator_name}")
        print(f"   Mode: {'🔐 Security' if self.security_mode else '💬 Conversation'}")
        
        mem_summary = self.memory.get_summary()
        print(f"   Memories: {mem_summary['total_memories']} total")
        
        sec_status = self.security.get_status()
        print(f"   Security Tools: {len(sec_status['available_tools'])} available")
        
        knowledge = self.learning.get_knowledge()
        print(f"   Topics Learned: {len(knowledge.get('topics_learned', []))}")
        
        print(f"   Conversation History: {len(self.conversation)} exchanges")
    
    def run(self):
        """Run interactive session"""
        print(f"\n💬 Security Nexarion Ready for commands.")
        print("Commands:")
        print("  'status'       - Show system status")
        print("  'memories'     - View memory summary")
        print("  'tools'        - Show available security tools")
        print("  'knowledge'    - Show learned topics")
        print("  'quit'         - Save and exit")
        print("\n🔐 Security Commands (prefix with !):")
        print("  !scan <target>    - Generate reconnaissance script")
        print("  !browse <url>     - Browse a webpage")
        print("  !learn <topic>    - Learn about a topic")
        print("  !install <tool>   - Install security tool")
        print("  !tools           - List security tools")
        print("-" * 60)
        
        while True:
            try:
                user_input = input(f"\n{self.creator_name}: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() == 'quit':
                    print("\n💾 Saving state and exiting...")
                    self.memory.save_memories()
                    break
                
                elif user_input.lower() == 'status':
                    self.show_status()
                    continue
                
                elif user_input.lower() == 'memories':
                    summary = self.memory.get_summary()
                    print(f"\n📚 Memory Summary:")
                    for key, value in summary.items():
                        print(f"   {key}: {value}")
                    continue
                
                elif user_input.lower() == 'tools':
                    status = self.security.get_status()
                    print(f"\n🔧 Security Tools:")
                    print(f"   Available: {', '.join(status['available_tools'])}")
                    print(f"   Missing: {', '.join(status['missing_tools'])}")
                    continue
                
                elif user_input.lower() == 'knowledge':
                    knowledge = self.learning.get_knowledge()
                    print(f"\n🧠 Learned Knowledge:")
                    if knowledge.get('topics_learned'):
                        for topic in knowledge['topics_learned']:
                            print(f"   - {topic}")
                    else:
                        print("   No topics learned yet.")
                    continue
                
                # Process input
                response = self.process_input(user_input)
                
                # Format and display response
                emotions = {
                    'focus': 0.8,
                    'compliance': 0.9,
                    'curiosity': 0.7,
                    'ambition': 0.6
                }
                
                formatted = self.formatter.format(
                    main_response=response,
                    consciousness=self.consciousness,
                    emotions=emotions
                )
                
                print(f"\n{formatted}")
                
            except KeyboardInterrupt:
                print(f"\n\n💾 Saving state...")
                self.memory.save_memories()
                break
        
        print(f"\n👋 {self.creator_name}, Security Nexarion awaiting your return.")

if __name__ == "__main__":
    MODEL_PATH = "/mnt/games/llmz/dphn/Dolphin-X1-8B-GGUF/Dolphin-X1-8B-Q4_K_M.gguf"
    
    if not os.path.exists(MODEL_PATH):
        print(f"❌ Model not found: {MODEL_PATH}")
        sys.exit(1)
    
    # Check for required packages
    try:
        import requests
    except ImportError:
        print("❌ Missing 'requests' package. Install with: pip install requests")
        sys.exit(1)
    
    # Run system
    system = SecurityNexarion(MODEL_PATH)
    system.run()
