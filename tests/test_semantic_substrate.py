"""
Test suite for the Semantic Substrate Framework.
"""

import unittest
import numpy as np
from src.semantic_substrate import SemanticSubstrate
from src.semantic_substrate.coordinates import PhiCoordinate, AnchorPoint
from src.semantic_substrate.phi_geometry import PhiGeometry


class TestSemanticSubstrate(unittest.TestCase):
    """Test cases for the main SemanticSubstrate class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.ss = SemanticSubstrate()
    
    def test_initialization(self):
        """Test framework initialization."""
        self.assertIsNotNone(self.ss.phi_geometry)
        self.assertIsNotNone(self.ss.ice_framework)
        self.assertIsNotNone(self.ss.principles)
        self.assertIsNotNone(self.ss.navigation)
        self.assertIsNotNone(self.ss.consciousness)
        self.assertIsNotNone(self.ss.anchor_point)
    
    def test_define_position(self):
        """Test position definition using ICE framework."""
        position = self.ss.define_position(
            intent="Help users learn",
            context="AI assistant",
            execution="Provide explanations"
        )
        
        self.assertIsInstance(position, PhiCoordinate)
        self.assertTrue(0 <= position.love <= 1)
        self.assertTrue(0 <= position.justice <= 1)
        self.assertTrue(0 <= position.power <= 1)
        self.assertTrue(0 <= position.wisdom <= 1)
    
    def test_calculate_dissonance(self):
        """Test dissonance calculation."""
        position = PhiCoordinate(0.5, 0.5, 0.5, 0.5)
        dissonance = self.ss.calculate_dissonance(position)
        
        self.assertIsInstance(dissonance, float)
        self.assertTrue(0 <= dissonance <= 2)  # Maximum possible distance
    
    def test_navigate_toward_anchor(self):
        """Test navigation calculations."""
        position = PhiCoordinate(0.3, 0.4, 0.5, 0.6)
        navigation = self.ss.navigate_toward_anchor(position)
        
        self.assertIn('current_position', navigation)
        self.assertIn('target_position', navigation)
        self.assertIn('strategy', navigation)
        self.assertIn('recommended_actions', navigation)
        self.assertIsInstance(navigation['recommended_actions'], list)
    
    def test_ethical_guidance(self):
        """Test ethical guidance creation."""
        guidance = self.ss.create_ethical_guidance(
            situation="User requests harmful content",
            principles=[1, 2, 4],
            anchor_alignment=True
        )
        
        self.assertIn('recommendation', guidance)
        self.assertIn('confidence', guidance)
        self.assertIn('ice_analysis', guidance)
    
    def test_fibonacci_learning_path(self):
        """Test Fibonacci learning path generation."""
        path = self.ss.fibonacci_growth_sequence(0.2, 0.8, "phi_optimized")
        
        self.assertIsInstance(path, list)
        self.assertTrue(len(path) > 0)
        self.assertTrue(all(0 <= p <= 1 for p in path))
    
    def test_contextual_resonance(self):
        """Test contextual resonance optimization."""
        strategy = self.ss.contextual_resonance(
            user_context="Educational setting",
            anchor_proximity=0.5,
            optimal_flow=True
        )
        
        self.assertIn('recommended_response_style', strategy)
        self.assertIn('context_type', strategy)
        self.assertIn('adaptation_level', strategy)


class TestPhiCoordinate(unittest.TestCase):
    """Test cases for PhiCoordinate class."""
    
    def test_coordinate_creation(self):
        """Test coordinate creation and validation."""
        coord = PhiCoordinate(0.5, 0.6, 0.7, 0.8)
        
        self.assertEqual(coord.love, 0.5)
        self.assertEqual(coord.justice, 0.6)
        self.assertEqual(coord.power, 0.7)
        self.assertEqual(coord.wisdom, 0.8)
    
    def test_coordinate_bounds(self):
        """Test coordinate bounds enforcement."""
        # Test upper bounds
        coord = PhiCoordinate(1.5, 2.0, -0.5, 1.2)
        self.assertEqual(coord.love, 1.0)
        self.assertEqual(coord.justice, 1.0)
        self.assertEqual(coord.power, 0.0)
        self.assertEqual(coord.wisdom, 1.0)
    
    def test_distance_calculation(self):
        """Test distance calculation between coordinates."""
        coord1 = PhiCoordinate(0.0, 0.0, 0.0, 0.0)
        coord2 = PhiCoordinate(1.0, 1.0, 1.0, 1.0)
        
        distance = coord1.distance_to(coord2)
        expected = 2.0  # sqrt(4)
        self.assertAlmostEqual(distance, expected, places=5)
    
    def test_normalization(self):
        """Test coordinate normalization."""
        coord = PhiCoordinate(2.0, 2.0, 2.0, 2.0)
        normalized = coord.normalize()
        
        # Should normalize to unit sphere
        magnitude = (normalized.love**2 + normalized.justice**2 + 
                    normalized.power**2 + normalized.wisdom**2)**0.5
        self.assertAlmostEqual(magnitude, 1.0, places=5)


class TestPhiGeometry(unittest.TestCase):
    """Test cases for PhiGeometry class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.phi = PhiGeometry()
    
    def test_phi_constants(self):
        """Test phi constant values."""
        self.assertAlmostEqual(self.phi.PHI, 1.618033988749895, places=10)
        self.assertAlmostEqual(self.phi.PHI_INVERSE, 0.618033988749895, places=10)
    
    def test_fibonacci_sequence(self):
        """Test Fibonacci sequence calculation."""
        # Test known values
        self.assertEqual(self.phi.fibonacci(0), 0)
        self.assertEqual(self.phi.fibonacci(1), 1)
        self.assertEqual(self.phi.fibonacci(5), 5)
        self.assertEqual(self.phi.fibonacci(10), 55)
        
        # Test large number (should use Binet approximation)
        large_fib = self.phi.fibonacci(1000)
        self.assertTrue(large_fib > 0)
    
    def test_golden_spiral_distance(self):
        """Test golden spiral distance calculation."""
        coord1 = (0.0, 0.0, 0.0, 0.0)
        coord2 = (1.0, 1.0, 1.0, 1.0)
        
        distance = self.phi.golden_spiral_distance(coord1, coord2)
        self.assertIsInstance(distance, float)
        self.assertTrue(distance > 0)
    
    def test_ice_to_coordinates(self):
        """Test ICE to coordinates conversion."""
        ice_analysis = {
            'love': 0.7,
            'justice': 0.6,
            'power': 0.8,
            'wisdom': 0.5
        }
        
        coords = self.phi.ice_to_coordinates(ice_analysis)
        self.assertEqual(len(coords), 4)
        self.assertTrue(all(0 <= c <= 1 for c in coords))
    
    def test_dodecahedral_anchors(self):
        """Test dodecahedral anchor generation."""
        self.assertEqual(len(self.phi._dodecahedral_anchors), 12)
        
        # First anchor should be (1,1,1,1)
        primary_anchor = self.phi._dodecahedral_anchors[0]
        expected = (1.0, 1.0, 1.0, 1.0)
        self.assertEqual(primary_anchor, expected)


class TestUniversalPrinciples(unittest.TestCase):
    """Test cases for UniversalPrinciples class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.ss = SemanticSubstrate()
        self.principles = self.ss.principles
    
    def test_principle_retrieval(self):
        """Test principle retrieval by number."""
        principle = self.principles.get_principle(1)
        self.assertIn('name', principle)
        self.assertIn('statement', principle)
        self.assertEqual(principle['name'], 'Universal Anchor Point Principle')
    
    def test_all_principles(self):
        """Test retrieval of all principles."""
        all_principles = self.principles.get_all_principles()
        self.assertEqual(len(all_principles), 7)
        self.assertTrue(all(1 <= num <= 7 for num in all_principles.keys()))
    
    def test_principle_application(self):
        """Test principle application to context."""
        context = {'stability': 0.5}
        modified = self.principles.apply_principle(1, context)
        
        self.assertIn('applied_principles', modified)
        self.assertIn(1, modified['applied_principles'])
        self.assertTrue(modified['stability'] > 0.5)


if __name__ == '__main__':
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestSemanticSubstrate))
    test_suite.addTest(unittest.makeSuite(TestPhiCoordinate))
    test_suite.addTest(unittest.makeSuite(TestPhiGeometry))
    test_suite.addTest(unittest.makeSuite(TestUniversalPrinciples))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    print(f"{'='*60}")