-- 8大类
SELECT 
j.rybh,j.xm,j.snbh,j.jsh,j.ay,j.emlx,
GROUP_CONCAT(a.content) as content 
FROM jbxx j
LEFT JOIN `alantop_案件类别` a ON FIND_IN_SET(a.code, j.ay)
JOIN `kst_8大案` c ON FIND_IN_SET(c.ay, a.code)
WHERE state = 'R8' AND FIND_IN_SET(c.ay, a.code)
-- AND j.emlx = '1'
GROUP BY j.rybh