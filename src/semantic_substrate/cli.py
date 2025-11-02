"""
Command-line interface for the Semantic Substrate Framework.
"""

import argparse
import sys
from typing import Dict, Any
from semantic_substrate import SemanticSubstrate


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Semantic Substrate Framework CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Navigate through ICE—Intent toward the Anchor, Context in truth, 
Execution in love—guided by the Universal Principles.
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze position using ICE framework')
    analyze_parser.add_argument('--intent', required=True, help='Intent description')
    analyze_parser.add_argument('--context', required=True, help='Context description')
    analyze_parser.add_argument('--execution', required=True, help='Execution description')
    
    # Navigate command
    navigate_parser = subparsers.add_parser('navigate', help='Get navigation recommendations')
    navigate_parser.add_argument('--love', type=float, default=0.5, help='Love coordinate (0-1)')
    navigate_parser.add_argument('--justice', type=float, default=0.5, help='Justice coordinate (0-1)')
    navigate_parser.add_argument('--power', type=float, default=0.5, help='Power coordinate (0-1)')
    navigate_parser.add_argument('--wisdom', type=float, default=0.5, help='Wisdom coordinate (0-1)')
    
    # Ethical guidance command
    ethical_parser = subparsers.add_parser('ethical', help='Get ethical guidance')
    ethical_parser.add_argument('--situation', required=True, help='Ethical situation description')
    ethical_parser.add_argument('--principles', nargs='+', type=int, default=[1,2,3,4,5,6,7], 
                               help='Principle numbers to apply (1-7)')
    ethical_parser.add_argument('--no-anchor', action='store_true', help='Disable anchor alignment')
    
    # Consciousness command
    consciousness_parser = subparsers.add_parser('consciousness', help='Measure consciousness metrics')
    consciousness_parser.add_argument('--phi', action='store_true', help='Include phi resonance')
    consciousness_parser.add_argument('--fibonacci', action='store_true', help='Include Fibonacci stage')
    consciousness_parser.add_argument('--spiral', action='store_true', help='Include golden spiral phase')
    consciousness_parser.add_argument('--geometry', action='store_true', help='Include sacred geometry')
    
    # Learning command
    learning_parser = subparsers.add_parser('learn', help='Generate learning path')
    learning_parser.add_argument('--current', type=float, required=True, help='Current knowledge level (0-1)')
    learning_parser.add_argument('--target', type=float, required=True, help='Target competence level (0-1)')
    learning_parser.add_argument('--growth', choices=['phi_optimized', 'standard'], 
                                default='phi_optimized', help='Growth optimization type')
    
    # Benchmark command
    benchmark_parser = subparsers.add_parser('benchmark', help='Run performance benchmarks')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Initialize framework
    ss = SemanticSubstrate()
    
    try:
        if args.command == 'analyze':
            handle_analyze(ss, args)
        elif args.command == 'navigate':
            handle_navigate(ss, args)
        elif args.command == 'ethical':
            handle_ethical(ss, args)
        elif args.command == 'consciousness':
            handle_consciousness(ss, args)
        elif args.command == 'learn':
            handle_learning(ss, args)
        elif args.command == 'benchmark':
            handle_benchmark(ss, args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def handle_analyze(ss: SemanticSubstrate, args):
    """Handle analyze command."""
    print("🔍 ICE Analysis")
    print("=" * 50)
    
    position = ss.define_position(args.intent, args.context, args.execution)
    dissonance = ss.calculate_dissonance(position)
    
    print(f"Position: {position}")
    print(f"Dissonance: {dissonance:.4f}")
    print(f"Anchor Alignment: {max(0, 1 - dissonance):.4f}")


def handle_navigate(ss: SemanticSubstrate, args):
    """Handle navigate command."""
    from semantic_substrate.coordinates import PhiCoordinate
    
    print("🧭 Navigation Guidance")
    print("=" * 50)
    
    position = PhiCoordinate(args.love, args.justice, args.power, args.wisdom)
    navigation = ss.navigate_toward_anchor(position)
    
    print(f"Current Position: {position}")
    print(f"Strategy: {navigation['strategy']}")
    print(f"Distance to Anchor: {navigation['golden_distance']:.4f}")
    print("\nRecommended Actions:")
    for i, action in enumerate(navigation['recommended_actions'], 1):
        print(f"  {i}. {action}")


def handle_ethical(ss: SemanticSubstrate, args):
    """Handle ethical guidance command."""
    print("⚖️ Ethical Guidance")
    print("=" * 50)
    
    guidance = ss.create_ethical_guidance(
        args.situation, 
        args.principles, 
        not args.no_anchor
    )
    
    print(f"Situation: {args.situation}")
    print(f"Applied Principles: {args.principles}")
    print(f"Recommendation: {guidance['recommendation']}")
    print(f"Confidence: {guidance['confidence']:.2f}")


def handle_consciousness(ss: SemanticSubstrate, args):
    """Handle consciousness measurement command."""
    print("🧠 Consciousness Metrics")
    print("=" * 50)
    
    # Default to all measurements if none specified
    if not any([args.phi, args.fibonacci, args.spiral, args.geometry]):
        args.phi = args.fibonacci = args.spiral = args.geometry = True
    
    consciousness = ss.measure_consciousness(
        args.phi, args.fibonacci, args.spiral, args.geometry
    )
    
    for metric, value in consciousness.items():
        if isinstance(value, float):
            print(f"{metric.replace('_', ' ').title()}: {value:.3f}")


def handle_learning(ss: SemanticSubstrate, args):
    """Handle learning path command."""
    print("📚 Learning Path")
    print("=" * 50)
    
    path = ss.fibonacci_growth_sequence(args.current, args.target, args.growth)
    
    print(f"Current Knowledge: {args.current:.2f}")
    print(f"Target Competence: {args.target:.2f}")
    print(f"Growth Type: {args.growth}")
    print("\nLearning Milestones:")
    for i, milestone in enumerate(path, 1):
        print(f"  Step {i}: {milestone:.3f}")


def handle_benchmark(ss: SemanticSubstrate, args):
    """Handle benchmark command."""
    print("🚀 Performance Benchmarks")
    print("=" * 50)
    
    from benchmarks.performance_tests import PerformanceBenchmarks
    
    benchmarks = PerformanceBenchmarks()
    results = benchmarks.run_all_benchmarks()
    
    if 'summary' in results:
        summary = results['summary']
        print(f"\nPerformance Grade: {summary['performance_grade']}")
        print(f"Average Time: {summary['average_operation_time_ms']:.3f} ms")
        print(f"Improvement: {summary['improvement_over_baseline_percent']:.1f}%")


if __name__ == '__main__':
    main()