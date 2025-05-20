#!/usr/bin/env python3
"""
Autonomous Blogging Pipeline
----------------------------
This script orchestrates the full blogging pipeline from keyword discovery to publishing and promotion.
"""

import os
import sys
import argparse
import logging
import json
import yaml
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("blog-automation")

class BlogPipeline:
    """Main pipeline controller for the autonomous blogging system."""
    
    def __init__(self, config_path="config.yaml"):
        """Initialize the pipeline with configuration."""
        self.config = self._load_config(config_path)
        self.modules = {}
        self._load_modules()
        
    def _load_config(self, config_path):
        """Load configuration from YAML file."""
        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            return {}
            
    def _load_modules(self):
        """Load all pipeline modules."""
        try:
            # Import modules dynamically
            from pipeline.keyword_discovery import KeywordDiscovery
            from pipeline.content_creation import ContentCreation
            from pipeline.grammar_check import GrammarStyleChecker
            from pipeline.visual_generator import VisualGenerator
            from pipeline.publisher import Publisher
            from pipeline.monetization import MonetizationManager
            from pipeline.social_promotion import SocialPromotion
            from pipeline.email_drafter import EmailDrafter
            from pipeline.analytics import AnalyticsTracker
            
            # Initialize modules
            self.modules["keyword"] = KeywordDiscovery(self.config.get("keyword_discovery", {}))
            self.modules["content"] = ContentCreation(self.config.get("content_creation", {}))
            self.modules["grammar"] = GrammarStyleChecker(self.config.get("grammar_check", {}))
            self.modules["visual"] = VisualGenerator(self.config.get("visual_generator", {}))
            self.modules["publish"] = Publisher(self.config.get("publisher", {}))
            self.modules["monetize"] = MonetizationManager(self.config.get("monetization", {}))
            self.modules["social"] = SocialPromotion(self.config.get("social_promotion", {}))
            self.modules["email"] = EmailDrafter(self.config.get("email_drafter", {}))
            self.modules["analytics"] = AnalyticsTracker(self.config.get("analytics", {}))
            
            logger.info("All modules loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load modules: {e}")
            
    def run(self, topic):
        """Run the full pipeline with the given topic."""
        logger.info(f"Starting pipeline for topic: {topic}")
        
        try:
            # 1. Keyword Discovery
            keywords = self.modules["keyword"].discover(topic)
            logger.info(f"Keywords discovered: {keywords}")
            
            # 2. Content Creation
            content = self.modules["content"].create(keywords)
            logger.info("Content created successfully")
            
            # 3. Grammar & Style Check
            content = self.modules["grammar"].check(content)
            logger.info("Grammar and style check completed")
            
            # 4. Visual Generation
            images = self.modules["visual"].generate(content)
            logger.info(f"Generated {len(images)} images")
            
            # 5. Publishing
            url = self.modules["publish"].publish(content, images)
            logger.info(f"Published to: {url}")
            
            # 6. Monetization
            monetized_content = self.modules["monetize"].apply(content, url)
            logger.info("Monetization applied")
            
            # 7. Social Promotion
            social_posts = self.modules["social"].promote(url, content)
            logger.info(f"Created {len(social_posts)} social media posts")
            
            # 8. Email Draft
            email_draft = self.modules["email"].draft(url, content)
            logger.info("Email newsletter draft created")
            
            # 9. Analytics Setup
            self.modules["analytics"].setup_tracking(url)
            logger.info("Analytics tracking configured")
            
            return {
                "status": "success",
                "url": url,
                "social_posts": social_posts,
                "email_draft": email_draft
            }
            
        except Exception as e:
            logger.error(f"Pipeline failed: {e}")
            return {
                "status": "error",
                "message": str(e)
            }

def main():
    """Main entry point for the pipeline script."""
    parser = argparse.ArgumentParser(description="Run the autonomous blogging pipeline")
    parser.add_argument("topic", help="The blog topic to process")
    parser.add_argument("--config", default="config.yaml", help="Path to configuration file")
    args = parser.parse_args()
    
    pipeline = BlogPipeline(args.config)
    result = pipeline.run(args.topic)
    
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "success" else 1

if __name__ == "__main__":
    sys.exit(main())
