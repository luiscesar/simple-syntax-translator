
set PYTHONPATH=.

rem type tests\resources\OneOne.txt | python tests\compiler\frontend\lexer\LexerTest.py

echo "========= WordTest ========"
python tests\compiler\frontend\lexer\WordTest.py

echo "========= IdTest ========="
python tests\compiler\frontend\inter\IdTest.py

echo "========= EnvTest ========="
python tests\compiler\frontend\symbols\EnvTest.py

echo "========= NodeTest ========="
python tests\compiler\frontend\inter\NodeTest.py

echo "========= ExprTest ========="
python tests\compiler\frontend\inter\ExprTest.py

echo "========= ConstantTest ========="
python tests\compiler\frontend\inter\ConstantTest.py



