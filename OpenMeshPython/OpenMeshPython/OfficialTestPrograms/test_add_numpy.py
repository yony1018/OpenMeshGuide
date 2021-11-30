import unittest
import openmesh

import numpy as np

class AddNumPy(unittest.TestCase):

    def setUp(self):
        self.points = np.array([[0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0]])
        self.fv_indices = np.array([[2, 1, 0], [2, 0, 3]])
        self.mesh = openmesh.TriMesh(self.points, self.fv_indices)

        # Test setup:
        #  1 === 2
        #  |   / |
        #  |  /  |
        #  | /   |
        #  0 === 3

        self.checkSetUp()

    def checkSetUp(self):
        self.assertEqual(self.mesh.n_vertices(), 4)
        self.assertEqual(self.mesh.n_edges(), 5)
        self.assertEqual(self.mesh.n_faces(), 2)
        self.assertEqual(self.mesh.points().shape, (4, 3))
        self.assertTrue(np.array_equal(self.mesh.points(), self.points))
        self.assertTrue(np.array_equal(self.mesh.fv_indices(), self.fv_indices))

    def checkAddVertices(self, new_points):
        self.assertEqual(self.mesh.n_vertices(), 10)
        self.assertEqual(self.mesh.n_edges(), 5)
        self.assertEqual(self.mesh.n_faces(), 2)
        self.assertEqual(self.mesh.points().shape, (10, 3))
        self.assertTrue(np.array_equal(self.mesh.points()[:4], self.points))
        self.assertTrue(np.array_equal(self.mesh.points()[4:], new_points))
        self.assertTrue(np.array_equal(self.mesh.fv_indices(), self.fv_indices))

    def checkAddVerticesAndFaces(self, new_points, new_faces):
        self.assertEqual(self.mesh.n_vertices(), 6)
        self.assertEqual(self.mesh.n_edges(), 9)
        self.assertEqual(self.mesh.n_faces(), 4)
        self.assertEqual(self.mesh.points().shape, (6, 3))
        self.assertTrue(np.array_equal(self.mesh.points()[:4], self.points))
        self.assertTrue(np.array_equal(self.mesh.points()[4:], new_points))
        self.assertTrue(np.array_equal(self.mesh.fv_indices()[:2], self.fv_indices))
        self.assertTrue(np.array_equal(self.mesh.fv_indices()[2:], new_faces))

    def test_resize_points(self):
        new_points = np.random.rand(6, 3)
        self.mesh.resize_points(10)
        self.mesh.points()[4:] = new_points
        self.checkAddVertices(new_points)

    def test_add_vertices(self):
        new_points = np.random.rand(6, 3)
        self.mesh.add_vertices(new_points)
        self.checkAddVertices(new_points)

    def test_add_vertices_wrong_shape(self):
        with self.assertRaises(RuntimeError):
            self.mesh.add_vertices(np.random.rand(6, 2))
        self.checkSetUp()
        with self.assertRaises(RuntimeError):
            self.mesh.add_vertices(np.random.rand(6, 4))
        self.checkSetUp()
        with self.assertRaises(RuntimeError):
            self.mesh.add_vertices(np.random.rand(6, 3, 3))
        self.checkSetUp()

    def test_add_vertices_empty_array(self):
        self.mesh.add_vertices(np.random.rand(0, 3))
        self.checkSetUp()

    def test_add_faces(self):
        new_vertices = [[2, 1, 0], [2, 0, 0]]
        new_faces = [[4, 2, 3], [4, 3, 5]]
        self.mesh.add_vertices(new_vertices)
        self.mesh.add_faces(new_faces)
        self.checkAddVerticesAndFaces(new_vertices, new_faces)

    def test_add_faces_wrong_shape(self):
        with self.assertRaises(RuntimeError):
            self.mesh.add_faces(np.arange(10).reshape(5, 2))
        self.checkSetUp()
        with self.assertRaises(RuntimeError):
            self.mesh.add_faces(np.arange(30).reshape(5, 3, 2))
        self.checkSetUp()

    def test_add_faces_empty_array(self):
        self.mesh.add_faces(np.random.rand(0, 3))
        self.checkSetUp()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AddNumPy)
    unittest.TextTestRunner(verbosity=2).run(suite)
