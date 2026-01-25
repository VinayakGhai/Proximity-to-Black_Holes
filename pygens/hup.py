from manim import *

class HeisenbergGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0,5,1], y_range=[0,5,1],
            x_length=7, y_length=5
        )
        self.add(axes)

        curve = axes.plot(lambda x: 1/(2*x), color=YELLOW)
        label = axes.get_graph_label(curve, label="Δp = ħ/2Δx")

        self.play(Create(curve), Write(label))
        self.wait(2)
