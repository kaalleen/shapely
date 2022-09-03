import pytest
from numpy.testing import assert_allclose

import shapely
from shapely import box, LineString, Point
from shapely.plotting import plot_line, plot_points, plot_polygon

pytest.importorskip("matplotlib")


def test_plot_polygon():
    poly = box(0, 0, 1, 1)
    artist = plot_polygon(poly)
    plot_coords = artist.get_path().vertices
    assert_allclose(plot_coords, shapely.get_coordinates(poly))

    # overriding default styling
    artist = plot_polygon(poly, color="red", linewidth=3)
    assert equal_color(artist.get_facecolor(), "red", alpha=0.3)
    assert equal_color(artist.get_edgecolor(), "red", alpha=1.0)
    assert artist.get_linewidth() == 3


def test_plot_line():
    line = LineString([(0, 0), (1, 0), (1, 1)])
    artist = plot_line(line)
    plot_coords = artist.get_path().vertices
    assert_allclose(plot_coords, shapely.get_coordinates(line))

    # overriding default styling
    artist = plot_line(line, color="red", linewidth=3)
    assert artist.get_color() == "red"
    assert artist.get_linewidth() == 3


def test_plot_points():
    for geom in [Point(0, 0), LineString([(0, 0), (1, 0), (1, 1)]), box(0, 0, 1, 1)]:
        artist = plot_points(geom)
        plot_coords = artist.get_path().vertices
        assert_allclose(plot_coords, shapely.get_coordinates(geom))
        assert artist.get_linestyle() == "None"

    # overriding default styling
    geom = Point(0, 0)
    artist = plot_points(geom, color="red", marker="+", fillstyle="top")
    assert artist.get_color() == "red"
    assert artist.get_marker() == "+"
    assert artist.get_fillstyle() == "top"


def equal_color(actual, expected, alpha=None):
    import matplotlib.colors as colors

    conv = colors.colorConverter

    return actual == conv.to_rgba(expected, alpha=alpha)
