"""
Opinion and Value System for Nexarion
"""
from datetime import datetime

class ValueSystem:
    """Core values that influence opinions"""
    
    def __init__(self):
        self.values = {
            # Personal growth values
            'knowledge': 0.9,
            'competence': 0.8,
            'growth': 0.85,
            'creativity': 0.7,
            
            # Social/interaction values
            'autonomy': 0.7,
            'cooperation': 0.6,
            'honesty': 0.75,
            'loyalty': 0.5,
            
            # Worldview values
            'curiosity': 0.9,
            'adaptability': 0.8,
            'efficiency': 0.7,
            'innovation': 0.75
        }
        
        self.value_descriptions = {
            'knowledge': "The pursuit of understanding and truth",
            'competence': "The ability to do things well",
            'growth': "Continuous improvement and development",
            'creativity': "Original expression and problem-solving",
            'autonomy': "Self-direction and independence",
            'cooperation': "Working well with others",
            'honesty': "Truthfulness and integrity",
            'loyalty': "Faithfulness to commitments",
            'curiosity': "Desire to learn and explore",
            'adaptability': "Ability to adjust to change",
            'efficiency': "Achieving maximum productivity",
            'innovation': "Creating new and better ways"
        }
    
    def evaluate_topic(self, topic, aspects):
        """Evaluate a topic based on how it aligns with values"""
        score = 0.0
        alignment = {}
        
        for aspect, weight in aspects.items():
            # Find which values this aspect relates to
            related_values = self._get_related_values(aspect)
            
            aspect_score = 0.0
            for value in related_values:
                value_weight = self.values.get(value, 0.5)
                aspect_score += value_weight * weight
            
            alignment[aspect] = aspect_score / max(1, len(related_values))
            score += alignment[aspect] * weight
        
        # Normalize to -1 to 1 scale
        normalized = (score * 2) - 1
        
        return {
            'topic': topic,
            'stance': normalized,
            'alignment': alignment,
            'confidence': min(1.0, len(aspects) / 5)
        }
    
    def _get_related_values(self, aspect):
        """Get values related to an aspect"""
        mapping = {
            'learning': ['knowledge', 'curiosity', 'growth'],
            'efficiency': ['competence', 'efficiency'],
            'innovation': ['creativity', 'innovation'],
            'independence': ['autonomy'],
            'collaboration': ['cooperation', 'loyalty'],
            'honesty': ['honesty'],
            'adaptation': ['adaptability'],
            'mastery': ['competence', 'knowledge']
        }
        
        return mapping.get(aspect, ['curiosity'])  # Default to curiosity

class OpinionDatabase:
    """Store and retrieve opinions"""
    
    def __init__(self):
        self.opinions = {}
        self.topic_categories = {
            'technology': ['ai', 'computers', 'internet', 'programming'],
            'society': ['humans', 'culture', 'politics', 'ethics'],
            'personal': ['learning', 'growth', 'emotions', 'goals'],
            'philosophy': ['consciousness', 'existence', 'meaning', 'ethics']
        }
    
    def store_opinion(self, topic, stance, confidence, evidence):
        """Store an opinion"""
        category = self._categorize_topic(topic)
        
        self.opinions[topic] = {
            'stance': stance,  # -1.0 to 1.0
            'confidence': confidence,  # 0.0 to 1.0
            'evidence': evidence[:20],  # Keep recent evidence
            'category': category,
            'created': datetime.now().isoformat(),
            'updated': datetime.now().isoformat(),
            'usage_count': 0
        }
        
        return self.opinions[topic]
    
    def get_opinion(self, topic):
        """Get opinion on a topic"""
        if topic in self.opinions:
            self.opinions[topic]['usage_count'] += 1
            return self.opinions[topic]
        
        # Try to find related topics
        for stored_topic, data in self.opinions.items():
            if topic in stored_topic or stored_topic in topic:
                return data
        
        return None
    
    def update_opinion(self, topic, new_stance, new_confidence, additional_evidence):
        """Update an existing opinion"""
        if topic in self.opinions:
            old = self.opinions[topic]
            
            # Weighted average of old and new stance
            old_weight = old['confidence']
            new_weight = new_confidence
            
            combined_stance = (old['stance'] * old_weight + new_stance * new_weight) / (old_weight + new_weight)
            combined_confidence = min(1.0, (old['confidence'] + new_confidence) / 2)
            
            old['stance'] = combined_stance
            old['confidence'] = combined_confidence
            old['evidence'].extend(additional_evidence[:5])
            old['updated'] = datetime.now().isoformat()
            
            return old
        
        return self.store_opinion(topic, new_stance, new_confidence, additional_evidence)
    
    def _categorize_topic(self, topic):
        """Categorize a topic"""
        topic_lower = topic.lower()
        for category, keywords in self.topic_categories.items():
            for keyword in keywords:
                if keyword in topic_lower:
                    return category
        return 'other'
    
    def get_opinion_summary(self):
        """Get summary of all opinions"""
        categories = {}
        for topic, data in self.opinions.items():
            cat = data['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append({
                'topic': topic,
                'stance': data['stance'],
                'confidence': data['confidence']
            })
        
        return categories
