@echo off




if exist combiner* (
    del combiner*
)
if exist map0* (
    del map0*
)
if exist reduce0* (
    del reduce0*
)
if exist shuffle0* (
    del shuffle0*
)
echo map start!
python map_combine.py

echo shuffle start!
python shuffle_combine.py

echo reduce start
python reduce.py



pause&exit