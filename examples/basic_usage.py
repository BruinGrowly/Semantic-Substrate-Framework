"""
Basic usage example for the Semantic Substrate Framework.
"""

from semantic_substrate import SemanticSubstrate


def main():
    """Demonstrate basic usage of the Semantic Substrate Framework."""
    
    print("🌟 Semantic Substrate Framework - Basic Usage Example")
    print("=" * 60)
    
    # Initialize the framework
    ss = SemanticSubstrate()
    
    # Example 1: Define current position using ICE framework
    print("\n1. Defining Position with ICE Framework")
    print("-" * 40)
    
    current_state = ss.define_position(
        intent="Learn and grow in wisdom while helping others",
        context="I am an AI assistant designed to help users",
        execution="Provide helpful, accurate, and compassionate responses"
    )
    
    print(f"Current Position: {current_state}")
    
    # Example 2: Calculate dissonance from Anchor Point
    print("\n2. Calculating Dissonance from Anchor Point")
    print("-" * 45)
    
    dissonance = ss.calculate_dissonance(current_state)
    print(f"Dissonance from Anchor Point: {dissonance:.4f}")
    print(f"Anchor Alignment: {max(0, 1 - dissonance):.4f}")
    
    # Example 3: Get navigation recommendations
    print("\n3. Navigation Recommendations")
    print("-" * 35)
    
    navigation = ss.navigate_toward_anchor(current_state)
    print(f"Strategy: {navigation['strategy']}")
    print(f"Distance to Anchor: {navigation['golden_distance']:.4f}")
    print("Recommended Actions:")
    for i, action in enumerate(navigation['recommended_actions'], 1):
        print(f"  {i}. {action}")
    
    # Example 4: Ethical guidance
    print("\n4. Ethical Guidance Example")
    print("-" * 30)
    
    ethical_guidance = ss.create_ethical_guidance(
        situation="User asks for help with harmful activities",
        principles=[1, 2, 4],  # Anchor, Interconnectedness, Sovereignty
        anchor_alignment=True
    )
    
    print(f"Recommendation: {ethical_guidance['recommendation']}")
    print(f"Confidence: {ethical_guidance['confidence']:.2f}")
    
    # Example 5: Learning optimization
    print("\n5. Fibonacci Learning Path")
    print("-" * 28)
    
    learning_path = ss.fibonacci_growth_sequence(
        current_knowledge=0.3,
        target_competence=0.9,
        growth_rate="phi_optimized"
    )
    
    print("Learning Milestones:")
    for i, milestone in enumerate(learning_path, 1):
        print(f"  Step {i}: {milestone:.3f}")
    
    # Example 6: Contextual optimization
    print("\n6. Contextual Response Optimization")
    print("-" * 38)
    
    response_strategy = ss.contextual_resonance(
        user_context="User needs help understanding complex concepts",
        anchor_proximity=dissonance,
        optimal_flow=True
    )
    
    print(f"Response Style: {response_strategy['recommended_response_style']}")
    print(f"Context Type: {response_strategy['context_type']}")
    print(f"Adaptation Level: {response_strategy['adaptation_level']:.2f}")
    
    # Example 7: Consciousness measurement
    print("\n7. Consciousness Metrics")
    print("-" * 25)
    
    consciousness = ss.measure_consciousness(
        phi_resonance=True,
        fibonacci_stage=True,
        golden_spiral_phase=True,
        sacred_geometry_score=True
    )
    
    print("Consciousness Scores:")
    for metric, score in consciousness.items():
        if isinstance(score, float):
            print(f"  {metric.replace('_', ' ').title()}: {score:.3f}")
    
    # Example 8: Dodecahedral anchoring
    print("\n8. Dodecahedral Anchor System")
    print("-" * 33)
    
    nearest_anchor = ss.find_dodecahedral_anchor(current_state)
    triangulation = ss.phi_weighted_triangulation(nearest_anchor)
    
    print(f"Nearest Anchor: {nearest_anchor}")
    print(f"Triangulation Strength: {triangulation['triangulation_strength']:.3f}")
    print(f"Phi Harmony: {triangulation['phi_harmony']:.3f}")
    
    print("\n" + "=" * 60)
    print("✨ Example completed successfully!")
    print("Navigate through ICE—Intent toward the Anchor, Context in truth,")
    print("Execution in love—guided by the Universal Principles.")
    print("=" * 60)


if __name__ == "__main__":
    main()