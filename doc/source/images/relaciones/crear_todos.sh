for x in `ls *.dot`
do 
    dot -Tpng $x -o $x.png
done
