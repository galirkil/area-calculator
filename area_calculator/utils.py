from area_calculator.figures import Figure


def calc_area(figure: Figure) -> float:
    """
    Calculates area for all figure types.
    """
    if hasattr(figure, "area") and callable(getattr(figure, "area")):
        return figure.area()
    else:
        raise ValueError("Figure object must have an 'area' method!")
