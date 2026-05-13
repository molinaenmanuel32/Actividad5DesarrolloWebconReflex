import reflex as rx

config = rx.Config(
    app_name="Actividad5DesarrolloWebconReflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)