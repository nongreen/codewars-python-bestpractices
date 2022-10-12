def likes(names):
    names_count = len(names)

    return {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {}, and {others} like this"
    }[min(4, names_count)].format(*names[:3], others=names_count-2)
