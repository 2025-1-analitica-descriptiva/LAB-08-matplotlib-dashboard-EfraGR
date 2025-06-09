# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    import os
    import pandas as pd
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    os.makedirs("docs", exist_ok=True)

    df = pd.read_csv("files/input/shipping-data.csv")

    def shipping_per_warehouse(df):
        plt.figure()
        counts = df["Warehouse_block"].value_counts()
        counts.plot.bar(
            title="Shipping per Warehouse",
            xlabel="Warehouse block",
            ylabel="Record Count",
            color="tab:blue",
            fontsize=8,
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.tight_layout()
        plt.savefig("docs/shipping_per_warehouse.png")

    def mode_of_shipment(df):
        plt.figure()
        counts = df["Mode_of_Shipment"].value_counts()
        counts.plot.pie(
            title="Mode of shipment",
            wedgeprops=dict(width=0.35),
            ylabel="",
            colors=["tab:blue", "tab:orange", "tab:green"],
        )
        plt.tight_layout()
        plt.savefig("docs/mode_of_shipment.png")

    def average_customer_rating(df):
        plt.figure()
        summary = df.groupby("Mode_of_Shipment")["Customer_rating"].describe()
        summary = summary[["mean", "min", "max"]]
        plt.barh(
            y=summary.index,
            width=summary["max"] - 1,
            left=summary["min"],
            height=0.9,
            color="lightgray",
            alpha=0.8,
        )
        colors = ["tab:green" if val >= 3 else "tab:orange" for val in summary["mean"]]
        plt.barh(
            y=summary.index,
            width=summary["mean"] - 1,
            left=summary["min"],
            color=colors,
            height=0.5,
        )
        plt.title("Average Customer Rating")
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.gca().spines["left"].set_color("gray")
        plt.gca().spines["bottom"].set_color("gray")
        plt.tight_layout()
        plt.savefig("docs/average_customer_rating.png")

    def weight_distribution(df):
        plt.figure()
        df["Weight_in_gms"].plot.hist(
            title="Shipped Weight Distribution",
            color="tab:orange",
            edgecolor="white",
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.tight_layout()
        plt.savefig("docs/weight_distribution.png")

    shipping_per_warehouse(df)
    mode_of_shipment(df)
    average_customer_rating(df)
    weight_distribution(df)

pregunta_01()