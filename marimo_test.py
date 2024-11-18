import marimo

__generated_with = "0.9.18"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def __(mo):
    mo.md("""# Marimo Test""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""## Tabs""")
    return


@app.cell
def __(cars, mo):
    mo.ui.tabs({
        "Cars data": cars,
        "Cars data 2": cars
    })
    return


@app.cell
def __():
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""## Plots""")
    return


@app.cell
def __(alt, vega_datasets):
    population = vega_datasets.data.population.url

    (
        alt.Chart(population)
        .mark_boxplot(extent='min-max')
        .encode(
            x='age:O',
            y='people:Q'
        )
    )
    return (population,)


@app.cell
def __(alt, vega_datasets):
    movies = vega_datasets.data.movies.url

    base = alt.Chart(movies)

    bar = base.mark_bar().encode(
        alt.X('IMDB_Rating:Q').bin().axis(None),
        y='count()'
    )

    rule = base.mark_rule(color='red').encode(
        x='mean(IMDB_Rating):Q',
        size=alt.value(5)
    )

    bar + rule
    return bar, base, movies, rule


@app.cell
def __(alt, vega_datasets):
    iris = vega_datasets.data.iris()

    alt.Chart(iris).transform_fold(
        [
            "petalWidth",
            "petalLength",
            "sepalWidth",
            "sepalLength",
        ],
        as_=["Measurement_type", "value"],
    ).transform_density(
        density="value",
        bandwidth=0.3,
        groupby=["Measurement_type"],
        extent=[0, 8],
    ).mark_area().encode(
        alt.X("value:Q"),
        alt.Y("density:Q"),
        alt.Row("Measurement_type:N"),
    ).properties(
        width=300, height=50
    )
    return (iris,)


@app.cell
def __():
    return


@app.cell
def __(alt, vega_datasets):
    alt.Chart(vega_datasets.data.cars(), width=100).transform_density(
        'Miles_per_Gallon',
        as_=['Miles_per_Gallon', 'density'],
        extent=[5, 50],
        groupby=['Origin']
    ).mark_area(orient='horizontal').encode(
        alt.X('density:Q')
            .stack('center')
            .impute(None)
            .title(None)
            .axis(labels=False, values=[0], grid=False, ticks=True),
        alt.Y('Miles_per_Gallon:Q'),
        alt.Color('Origin:N'),
        alt.Column('Origin:N')
            .spacing(0)
            .header(titleOrient='bottom', labelOrient='bottom', labelPadding=0)
    ).configure_view(
        stroke=None
    )
    return


@app.cell
def __(alt, vega_datasets):
    seattle_weather = vega_datasets.data.seattle_weather.url

    step = 20
    overlap = 1

    alt.Chart(seattle_weather, height=step).transform_timeunit(
        Month='month(date)'
    ).transform_joinaggregate(
        mean_temp='mean(temp_max)', groupby=['Month']
    ).transform_bin(
        ['bin_max', 'bin_min'], 'temp_max'
    ).transform_aggregate(
        value='count()', groupby=['Month', 'mean_temp', 'bin_min', 'bin_max']
    ).transform_impute(
        impute='value', groupby=['Month', 'mean_temp'], key='bin_min', value=0
    ).mark_area(
        interpolate='monotone',
        fillOpacity=0.8,
        stroke='lightgray',
        strokeWidth=0.5
    ).encode(
        alt.X('bin_min:Q')
            .bin('binned')
            .title('Maximum Daily Temperature (C)'),
        alt.Y('value:Q')
            .axis(None)
            .scale(range=[step, -step * overlap]),
        alt.Fill('mean_temp:Q')
            .legend(None)
            .scale(domain=[30, 5], scheme='redyellowblue')
    ).facet(
        row=alt.Row('Month:T')
            .title(None)
            .header(labelAngle=0, labelAlign='left', format='%B')
    ).properties(
        title='Seattle Weather',
        bounds='flush'
    ).configure_facet(
        spacing=0
    ).configure_view(
        stroke=None
    ).configure_title(
        anchor='end'
    )
    return overlap, seattle_weather, step


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __(alt, cars, mo):
    chart = (
        alt.Chart(cars)
        .mark_point()
        .encode(
            x=alt.X("Horsepower", type="quantitative"),
            y=alt.Y("Miles_per_Gallon", type="quantitative"),
            color="Origin"
        )
        .properties(width="container")
    )

    chart = mo.ui.altair_chart(chart)
    return (chart,)


@app.cell
def __(chart):
    chart
    return


@app.cell
def __(chart, mo):
    mo.vstack([chart, chart.value.head()])
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __(cars, mo):
    mpg_range_slider = mo.ui.range_slider.from_series(cars["Miles_per_Gallon"])
    return (mpg_range_slider,)


@app.cell
def __(cars, mo):
    origin_multiselect = mo.ui.multiselect.from_series(cars["Origin"])
    return (origin_multiselect,)


@app.cell
def __(alt, cars, mo, mpg_range_slider, origin_multiselect, pl):
    cars_alt_data = (
        cars
        .filter(pl.col("Miles_per_Gallon").is_between(mpg_range_slider.value[0], mpg_range_slider.value[1]))
        .filter(pl.col("Origin").is_in(origin_multiselect.value))
    )

    car_chart = mo.ui.altair_chart(
        alt.Chart(cars_alt_data)
        .mark_point()
        .encode(
            x="Horsepower",
            y="Miles_per_Gallon",
            color="Origin"
        )
    )
    return car_chart, cars_alt_data


@app.cell
def __(car_chart, mo, mpg_range_slider, origin_multiselect):
    mo.hstack(
        [
            mo.vstack([
                mo.md(f"Choose a value for MPG: {mpg_range_slider}"),
                mo.md(f"Choose which origins to include: {origin_multiselect}"),
                car_chart
            ]),
            car_chart.value.head(5),
        ]
    )
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""## Great Tables""")
    return


@app.cell
def __(pl):
    random_numbers_df = pl.DataFrame(
        {
            "i": range(1, 5),
            "lines": [
                "20 23 6 7 37 23 21 4 7 16",
                "2.3 6.8 9.2 2.42 3.5 12.1 5.3 3.6 7.2 3.74",
                "-12 -5 6 3.7 0 8 -7.4",
                "2 0 15 7 8 10 1 24 17 13 6",
            ]
        }
        ).with_columns(bars=pl.col("lines"))
    return (random_numbers_df,)


@app.cell
def __(GT, mo, random_numbers_df):
    gtable = (
        GT(random_numbers_df, rowname_col="i")
        .fmt_nanoplot(columns="lines", plot_type="line")
        .fmt_nanoplot(columns="bars", plot_type="bar")
    )

    mo.hstack([gtable, random_numbers_df])
    return (gtable,)


@app.cell
def __(GT, html, sza_pivot):
    (
        GT(sza_pivot, rowname_col="month")
        .data_color(
            domain=[90, 0],
            palette=["rebeccapurple", "white", "orange"],
            na_color="white",
        )
        .tab_header(
            title="Solar Zenith Angles from 05:30 to 12:00",
            subtitle=html("Average monthly values at latitude of 20&deg;N."),
        )
        .sub_missing(missing_text="")
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""## Mermaid Diagrams""")
    return


@app.cell
def __():
    diagram = '''
    graph TD
        A[Square Rect] -- Link text --> B((Circle))
    '''
    return (diagram,)


@app.cell
def __(diagram, mo):
    mo.mermaid(diagram)
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""## UI Table""")
    return


@app.cell(hide_code=True)
def __(cars, mo):
    mo.ui.table(cars)
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""## UI DataFrame""")
    return


@app.cell(hide_code=True)
def __(cars, mo):
    mo.ui.dataframe(cars)
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""## UI Data explorer""")
    return


@app.cell(hide_code=True)
def __(cars, mo):
    mo.ui.data_explorer(cars)
    return


@app.cell
def __():
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""## SQL""")
    return


@app.cell(hide_code=True)
def __(cars, mo):
    _df = mo.sql(
        f"""
        (
        SELECT *
        FROM cars
        WHERE Cylinders <= 6
        )
        """
    )
    return


@app.cell
def __():
    # mo.sql(
    #     """
    #     SELECT TOP 10 *
    #     FROM read_parquet('example.parquet')
    #     """
    # )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""## Data""")
    return


@app.cell
def __(pl, sza, vega_datasets):
    cars = pl.DataFrame(vega_datasets.data.cars())

    sza_pivot = (
        pl.from_pandas(sza)
        .filter((pl.col("latitude") == "20") & (pl.col("tst") <= "1200"))
        .select(pl.col("*").exclude("latitude"))
        .drop_nulls()
        .pivot(values="sza", index="month", on="tst", sort_columns=True)
    )
    return cars, sza_pivot


@app.cell(hide_code=True)
def __(mo):
    mo.md("""## Setup""")
    return


@app.cell
def __():
    import os
    import sys
    import datetime as dt
    from pathlib import Path
    import warnings
    import importlib
    from pprint import pprint

    import marimo as mo
    import polars as pl
    import polars.selectors as cs
    import duckdb
    import sidetable as stb
    import altair as alt
    import vega_datasets
    from great_tables import GT, html, loc, style
    from great_tables.data import sza
    return (
        GT,
        Path,
        alt,
        cs,
        dt,
        duckdb,
        html,
        importlib,
        loc,
        mo,
        os,
        pl,
        pprint,
        stb,
        style,
        sys,
        sza,
        vega_datasets,
        warnings,
    )


@app.cell
def __(Path, os, pl):
    # pl.Config.set_tbl_formatting('NOTHING')
    # pl.Config.set_float_precision(3)
    # pl.Config.set_fmt_str_lengths(20)
    # pl.Config.set_tbl_hide_column_data_types(False)
    # pl.Config.save_to_file('pl_config.json')

    cwd = Path(os.getcwd())
    pl_config_path = Path(cwd, "pl_config.json")
    pl.Config.load_from_file(pl_config_path)
    return cwd, pl_config_path


if __name__ == "__main__":
    app.run()
