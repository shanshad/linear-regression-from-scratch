#parameters.py

def calculate_regression_params(points):
    sum_x = sum(p.x for p in points)
    sum_y = sum(p.y for p in points)
    sum_xy = sum(p.xy() for p in points)
    sum_xsqr = sum(p.xsqr() for p in points)
    n = len(points)
    return n,sum_x,sum_xsqr,sum_y,sum_xy
