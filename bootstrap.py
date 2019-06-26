import coords
import figures

if __name__ == "__main__":

    figures_one = figures.FigureDrawer()
    figures_one.clear()

    # figures_one.print_cross()
    # figures.print_image(coords.coords_panther, ws, 0, 0, 2)
    # figures.print_image(coords.coords_sponge, ws, 0, 0, 2)
    # figures.print_image(coords.coords_sonic, -30, 30, 1)
    # figures.print_image(coords.coords_scooby, -30, -30, 1)
    # figures.print_image(coords.coords_bart, ws, -20, 0, 2)
    # figures.print_image(coords.coords_monkey, ws, 25, -20, 2)
    # figures.print_image(coords.coords_homer, ws, 20, 0, 2)
    # figures_one.print_image(coords.coords_phineas, -35, 30, 1)
    figures_one.print_image(coords.coords_mario, 0, -20, 1.5)
    # figures_one.print_image(coords.coords_pikatchu, 35, -30, 1)
    # figures_one.print_image(coords.coords_kermit, 35, 30, 1)
    # figures_one.print_image(coords.coords_ferb, -35, -30, 1)

    wooloo = ("\U0001F411", "Symbola")
    slack = ("\uf198", "brands")

    figures_one.print_text(wooloo, -31.65, 7.25, 0.6)
    figures_one.print_text(slack, -5, 23.5, 0.5)


