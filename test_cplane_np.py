import cplane_np
import numpy as np

def test_cplane_np():
    a = cplane_np.ListComplexPlane(xmin = 10, xmax = 15, xlen = 3, ymin =2, ymax = 8, ylen = 3)
    np.testing.assert_almost_equal(a.plane, [10.0+2.j, 12.5+2.j, 15.0+2.j, 10.0+5.j, 12.5+5.j, 15.0+5.j, 10.0+8.j, 12.5+8.j, 15.0+8.j])
    
    ff = lambda x: x**2
    a.apply(ff)
    np.testing.assert_almost_equal(a.plane, [96.00 +40.j, 152.25 +50.j, 221.00 +60.j, 75.00+100.j, 131.25+125.j, 200.00+150.j, 36.00+160.j, 92.25+200.j, 161.00+240.j])
    
    a.zoom(newxmin = 5, newxmax = 10, newxlen =3, newymin =5, newymax = 10, newylen = 3)
    np.testing.assert_almost_equal(a.plane, [0.00 +50.j, 31.25 +75.j, 75.00+100.j, -31.25 +75.j, 0.00+112.5j, 43.75+150.j, -75.00+100.j, -43.75+150.j, 0.00+200.j])
    
    a.refresh()
    np.testing.assert_almost_equal(a.plane, [5.0 +5.j , 7.5 +5.j, 10.0 +5.j, 5.0 +7.5j, 7.5 +7.5j, 10.0 +7.5j, 5.0+10.j, 7.5+10.j, 10.0+10.j])