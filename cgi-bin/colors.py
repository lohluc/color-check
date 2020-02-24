color_info = {
    "red" : "#ff0000",
    "darkred" :"#8b0000",
    "lightsalmon" : "#ffa07a",
    "salmon" : "#fa8072",
    "darksalmon" : "#e9967a",
    "ligthcoral" : "#f08080",
    "indianred" : "#cd5c5c",
    "crimson" : "#dc143c",
    "firebrick" : "#b22222"
}

color_hex = {
    y : x for x,y in color_info.items()
}

color_info.update(color_hex)
