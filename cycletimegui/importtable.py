def import_table(value):
    return {
                "workID": "",
                "parts": {
                    "productID": value[1],
                    "module": float(value[4]),
                    "normPressAng_d": int(value[4]),
                    "normPressAng_m": int(value[5]),
                    "normPressAng_s": int(value[6]),
                    "starts": int(value[9]),
                    "pitchDia": float(value[7]),
                    "outDia": float(value[8]),
                    "rootDia": float(value[10]),
                    "leadAng_d": int(value[12]),
                    "leadAng_m": int(value[13]),
                    "leadAng_s": int(value[14]),
                    "toothThick": float(value[22]),
                    "threadLen": float(value[20])
                },
                "machining": [
                    {
                        "passes": int(value[77]),
                        "feedForw": float(value[79]),
                        "feedBack": float(value[80]),
                        "infeedForw": float(value[82]),
                        "infeedBack": float(value[84]),
                        "infeedTotal": 0,
                        "plunge": float(value[123]),
                        "speed": 0,
                        "dressPass": int(value[68]),
                        "dressInfeed": float(value[70]),
                        "dressFeed": float(value[72]),
                        "dressFrq": int(value[75])
                    },
                    {
                        "passes": int(value[78]),
                        "feedForw": float(value[106]),
                        "feedBack": float(value[107]),
                        "infeedForw": float(value[9]),
                        "infeedBack": float(value[83]),
                        "infeedTotal": 0,
                        "plunge": float(value[85]),
                        "speed": 0,
                        "dressPass": int(value[69]),
                        "dressInfeed": float(value[71]),
                        "dressFeed": float(value[73]),
                        "dressFrq": int(value[76])
                    },
                    {
                        "passes": int(value[134]),
                        "feedForw": float(value[135]),
                        "feedBack": float(value[136]),
                        "infeedForw": float(value[137]),
                        "infeedBack": float(value[138]),
                        "infeedTotal": 0,
                        "plunge": float(value[140]),
                        "speed": 0,
                        "dressPass": int(value[142]),
                        "dressInfeed": float(value[143]),
                        "dressFeed": float(value[144]),
                        "dressFrq": int(value[145])
                    },
                    {
                        "passes": int(value[146]),
                        "feedForw": float(value[147]),
                        "feedBack": float(value[148]),
                        "infeedForw": float(value[150]),
                        "infeedBack": float(value[151]),
                        "infeedTotal": 0,
                        "plunge": float(value[152]),
                        "speed": 0,
                        "dressPass": int(value[154]),
                        "dressInfeed": float(value[155]),
                        "dressFeed": float(value[156]),
                        "dressFrq": int(value[157])
                    }
                ]
            }