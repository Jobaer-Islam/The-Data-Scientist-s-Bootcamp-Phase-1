"""
Concept: Modularity
Functions should do ONE thing and return results.
"""

def calculate_area(radius: float) -> float:
    """Returns the area of a circle."""
    if radius < 0:
        return 0
    return 3.14 * radius * radius


def main():
    r = 5
    area = calculate_area(r)
    print("Area:", area)


main()
