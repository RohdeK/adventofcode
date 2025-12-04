from archive.y2023.puzzles.day_20.load_inputs import input_reader
from archive.y2023.puzzles.day_20.solution_part_1 import ConjunctionModule, FlipFlopModule, Orchestrator


def test_example():
    print("\n")
    test_input = input_reader.from_file("../input.txt")

    orch = Orchestrator()
    orch.add_modules(test_input)

    prev_state = None

    for i in range(10000):
        # print("-------------------------------------------")
        # print("Press", i + 1)
        orch.press_button()

        # continue
        state = {name: state.value for name, state in orch.modules["db"].remembered_states.items()}
        if state != prev_state:
            print("Press", i + 1)
            print(state)
            # print("Press", i + 1, state["rz"])
        prev_state = state

        """
        [gf]
        zd 2**3  is LO if P % 16 < 8 else HI
        qq 2**4 is LO if P % 32 < 16 else HI
        fn 2**10 is LO if P % 2048 < 1024 else HI
        tj 2**8 is LO if P % 512 < 256 else HI
        ln == qq 2**4 is LO if P % 32 < 16 else HI
        vl 2**1 is LO if P % 4 < 2 else HI
        sr 2**0 is LO if P % 2 < 1 else HI
        lc 2**9 is LO if P % 1024 < 512 else HI
        gm 2**7 is LO if P % 256 < 128 else HI
        pr 2**11 is LO if P % 4096 < 2048 else HI
        
        period = 2048 + 1024 + 512 + 256 + 128 + 32 + 16 + 8 + 2 + 1 = 4027
        
        [qx]
        kt 2**3  is LO if P % 16 < 8 else HI
        bf 2**10 is LO if P % 2048 < 1024 else HI
        jd 2**7 is LO if P % 256 < 128 else HI
        bx 2**0 is LO if P % 2 < 1 else HI
        cl 2**9 is LO if P % 1024 < 512 else HI
        qp 2**1 is LO if P % 4 < 2 else HI
        pf 2**11 is LO if P % 4096 < 2048 else HI
        rz 2**4 is LO if P % 32 < 16 else HI
        
        period = 2048 + 1024 + 512 + 128 + 16 + 8 + 2 + 1 = 3739

        [vc]
        vz 2**6 is LO if P % 128 < 64 else HI
        qk 2**11 is LO if P % 4096 < 2048 else HI
        sb 2**4 is LO if P % 32 < 16 else HI
        cr 2**7 is LO if P % 256 < 128 else HI
        pm 2**10 is LO if P % 2048 < 1024 else HI
        cd 2**9 is LO if P % 1024 < 512 else HI
        hd 2**0 is LO if P % 2 < 1 else HI

        period = 2048 + 1024 + 512 + 128 + 64 + 16 + 1 = 3793

        [db]
        pl 2**6 is LO if P % 128 < 64 else HI
        xm 2**11 is LO if P % 4096 < 2048 else HI
        nn 2**4 is LO if P % 32 < 16 else HI
        qj 2**10 is LO if P % 2048 < 1024 else HI
        mc 2**1 is LO if P % 4 < 2 else HI
        jz 2**9 is LO if P % 1024 < 512 else HI
        ch 2**0 is LO if P % 2 < 1 else HI
        bp 2**8 is LO if P % 512 < 256 else HI

        period = 2048 + 1024 + 512 + 256 + 64 + 16 + 2 + 1 = 3923

        [all]
        qf = low on 4027
        xn = invert gf = high on 4027
        qn = invert vc = high on 3793
        xf = invert db = high on 3923
        qx = low on 3739
        zl = invert qx = high on 3739
        db = low on 3923
        th
        vc = low on 3793
        
        
        rx low if 
        th inputs are all high
        zl high every 3739
        xn high every 4027
        qn high every 3793
        xf high every 3923
        """

