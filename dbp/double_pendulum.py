import numpy as np
from manim import *

# -----------------------------
# Physics
# -----------------------------
g = 9.81
l1 = l2 = 2.0
m1 = m2 = 1.0
dt = 0.02

def accel(t1, w1, t2, w2):
    d = t1 - t2
    den = (2*m1 + m2 - m2*np.cos(2*d))

    a1 = (
        -g*(2*m1+m2)*np.sin(t1)
        - m2*g*np.sin(t1-2*t2)
        - 2*np.sin(d)*m2*(w2**2*l2 + w1**2*l1*np.cos(d))
    ) / (l1*den)

    a2 = (
        2*np.sin(d)*(w1**2*l1*(m1+m2)
        + g*(m1+m2)*np.cos(t1)
        + w2**2*l2*m2*np.cos(d))
    ) / (l2*den)

    return a1, a2

def step(state):
    t1,w1,t2,w2 = state
    a1,a2 = accel(t1,w1,t2,w2)

    w1h = w1 + a1*dt/2
    w2h = w2 + a2*dt/2
    t1 += w1h*dt
    t2 += w2h*dt
    a1n,a2n = accel(t1,w1h,t2,w2h)

    w1 = w1h + a1n*dt/2
    w2 = w2h + a2n*dt/2
    return np.array([t1,w1,t2,w2])

# -----------------------------
# Scene
# -----------------------------
class DoublePendulumExplained(Scene):
    def construct(self):

        title = Text("A Double Pendulum", font_size=42)
        subtitle = Text("Same laws. Different futures.", font_size=28)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        origin = UP*2

        # Initial states (almost identical)
        sA = np.array([PI/2, 0, PI/2, 0])
        sB = np.array([PI/2+1e-4, 0, PI/2, 0])

        def pendulum(color):
            r1 = Line(origin, origin, stroke_width=3)
            r2 = Line(origin, origin, stroke_width=3)
            b1 = Dot(radius=0.06, color=color)
            b2 = Dot(radius=0.06, color=color)
            return r1,r2,b1,b2

        A = pendulum(BLUE)
        B = pendulum(RED)

        label = Text("Initial difference: 0.0001 rad", font_size=24)
        label.to_edge(DOWN)

        self.add(*A, *B, label)

        # Phase space
        axes = Axes(
            x_range=[-PI, PI],
            y_range=[-8, 8],
            x_length=5,
            y_length=3,
        ).to_corner(DOWN+RIGHT)

        axes_labels = axes.get_axis_labels(
            MathTex(r"\theta"), MathTex(r"\dot{\theta}")
        )

        pathA = VMobject(stroke_color=BLUE, stroke_width=1)
        pathB = VMobject(stroke_color=RED, stroke_width=1)

        pathA.set_points_as_corners([axes.c2p(sA[0], sA[1])])
        pathB.set_points_as_corners([axes.c2p(sB[0], sB[1])])

        self.play(FadeIn(axes), FadeIn(axes_labels))
        self.add(pathA, pathB)

        def update(mob, dt_):
            nonlocal sA, sB
            sA = step(sA)
            sB = step(sB)

            for s, P, path in [(sA,A,pathA),(sB,B,pathB)]:
                t1,w1,t2,w2 = s
                p1 = origin + l1*np.array([np.sin(t1),-np.cos(t1),0])
                p2 = p1 + l2*np.array([np.sin(t2),-np.cos(t2),0])

                P[0].put_start_and_end_on(origin,p1)
                P[1].put_start_and_end_on(p1,p2)
                P[2].move_to(p1)
                P[3].move_to(p2)

                path.add_points_as_corners([axes.c2p(t1,w1)])

        self.add_updater(update)

        explanation = Text(
            "The equations are deterministic.\nThe outcome is not predictable.",
            font_size=28
        ).to_edge(UP)

        self.wait(5)
        self.play(Write(explanation))
        self.wait(10)
