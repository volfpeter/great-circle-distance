[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

# Great circle distance

Simple great circle distance calculation package

## Usage

```python
from great_circle_distance import PlanetRadius, great_circle_distance

stonehenge = (51.178939, -1.825941)
great_pyramid_of_giza = (29.979123, 31.134234)

print(
    "Distance between Stonehenge and the Great Pyramid of Giza is "
    f"{great_circle_distance(stonehenge, great_pyramid_of_giza)} kilometers or "
    f"{great_circle_distance(stonehenge, great_pyramid_of_giza, radius=PlanetRadius.earth_mi)} miles."
)
```

## License - MIT

The library is open-sourced under the conditions of the MIT [license](https://choosealicense.com/licenses/mit/).
