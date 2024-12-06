import pygame as II1111II1;from random import randint as II1I11I1I;III1III11=not();III11II11=not(not());II1111II1.init();II1111I1I=II1111II1.display.set_mode((sum(range(51))+5,sum(range(39))-21));I111II111=II1111II1.time.Clock();II11II11I=not(not(not(II1I11I1I(int(),int(not())))));
if not II11II11I==III1III11:raise Exception('The game did not launch correctly because we decided you do not deserve to play it. Please try again later.');
I1111IIII=sum({2,3,5})*3;II1111II1.font.init();II1I1I1I1=II1111II1.font.SysFont(chr(82)+chr(111)+chr(98)+chr(111)+chr(116)+chr(111),40);exec("I1IIII11I=[648,360]");IIIII1III='11III11I1';I111II1I1='1111I1111';IIII11I11=list();III111II1=list();I11IIII1I=list();IIII11I1I=int();print(chr(sum(range(ord(min(str(not())))))));II1III11I=list();IIII1I11I=ord('Ĭ');I111I11II=IIII1I11I;
while II11II11I==III1III11:
    for I1III11II in II1111II1.event.get():
        if I1III11II.type==II1111II1.QUIT:exec(chr(113)+"u"+chr(105)+"t()");
    IIIII1II1=II1111II1.key.get_pressed();
    if IIIII1II1[II1111II1.K_RIGHT]and(IIIII1III=='1II1IIII1'or(IIIII1III=='1111IIIII'))and(I111II1I1=='1111I1111'):I111II1I1='11III11I1';
    elif IIIII1II1[II1111II1.K_LEFT]and(IIIII1III=='1II1IIII1'or(IIIII1III=='1111IIIII'))and(I111II1I1=='1111I1111'):I111II1I1='111III11I';
    elif IIIII1II1[II1111II1.K_DOWN]and(IIIII1III=='111III11I'or(IIIII1III=='11III11I1'))and(I111II1I1=='1111I1111'):I111II1I1='1111IIIII';
    elif IIIII1II1[II1111II1.K_UP]and(IIIII1III=='111III11I'or(IIIII1III=='11III11I1'))and(I111II1I1=='1111I1111'):I111II1I1='1II1IIII1';
    if I111II1I1=='11III11I1'and(I1IIII11I[int(not())]%I1111IIII==int()):IIIII1III='11III11I1';I111II1I1='1111I1111';
    elif I111II1I1=='111III11I'and(I1IIII11I[int(not())]%I1111IIII==int()):IIIII1III='111III11I';I111II1I1='1111I1111';
    elif I111II1I1=='1111IIIII'and(I1IIII11I[int()]%I1111IIII==int()):IIIII1III='1111IIIII';I111II1I1='1111I1111';
    elif I111II1I1=='1II1IIII1'and(I1IIII11I[int()]%I1111IIII==int()):IIIII1III='1II1IIII1';I111II1I1='1111I1111';
    try:II1111I1I.blit(II1111II1.transform.scale(II1111II1.image.load('iusghipdrwhpugsdfpiuogdhniopu  zsgdfgdsg???;;.jpg'),((sum(range(51))+5,sum(range(39))-21))),(int(),int()));
    except:II1111I1I.blit(II1111II1.transform.scale(II1111II1.image.load('iusghipdrwhpugsdfpiuogdhniopu  zsgdfgdsg___;;.jpg'),((sum(range(51))+5,sum(range(39))-21))),(int(),int()));
    if IIII1I11I==int():II1III11I.append([II1I11I1I(2,(sum(range(51))+5)//I1111IIII-2)*I1111IIII,II1I11I1I(2,(sum(range(39))-21)//I1111IIII-2)*I1111IIII]);IIII1I11I=I111I11II;
    IIII1I11I=IIII1I11I-int(not());
    for I1I1111II in II1III11I:
        II1111II1.draw.circle(II1111I1I,(int(),255,int()),(I1I1111II[int()],I1I1111II[int(not())]),15);
        I1II1I1I1=(abs(I1IIII11I[int()]-I1I1111II[int()])**2+abs(I1IIII11I[int(not())]-I1I1111II[int(not())])**2)**0.5;
        if I1II1I1I1<30:
            II1III11I.remove(I1I1111II);
            IIII11I1I=IIII11I1I+int(not());
            if I111I11II>int('A',16):I111I11II=I111I11II-5;
    I1111III1=II1I1I1I1.render('Score: '+str(IIII11I1I),III11II11,(255,)*3);II1111I1I.blit(I1111III1,(10,)*2);II1111II1.draw.circle(II1111I1I,(255,int(),int()),(I1IIII11I[int()],I1IIII11I[int(not())]),15);
    if IIIII1III=='11III11I1':I1IIII11I[int()]=I1IIII11I[int()]+3;II1111II1.draw.circle(II1111I1I,(int(),)*3,(I1IIII11I[int()]+10,I1IIII11I[int(not())]+12),10);II1111II1.draw.circle(II1111I1I,(int(),)*3,(I1IIII11I[int()]+10,I1IIII11I[int(not())]-12),10);
    elif IIIII1III=='111III11I':I1IIII11I[int()]=I1IIII11I[int()]-3;II1111II1.draw.circle(II1111I1I,(int(),)*3,(I1IIII11I[int()]-10,I1IIII11I[int(not())]+12),10);II1111II1.draw.circle(II1111I1I,(int(),)*3,(I1IIII11I[int()]-10,I1IIII11I[int(not())]-12),10);
    elif IIIII1III=='1111IIIII':I1IIII11I[int(not())]=I1IIII11I[int(not())]+3;II1111II1.draw.circle(II1111I1I,(int(),)*3,(I1IIII11I[int()]+12,I1IIII11I[int(not())]+10),10);II1111II1.draw.circle(II1111I1I,(int(),)*3,(I1IIII11I[int()]-12,I1IIII11I[int(not())]+10),10);
    elif IIIII1III=='1II1IIII1':I1IIII11I[int(not())]=I1IIII11I[int(not())]-3;II1111II1.draw.circle(II1111I1I,(int(),)*3,(I1IIII11I[int()]+12,I1IIII11I[int(not())]-10),10);II1111II1.draw.circle(II1111I1I,(int(),)*3,(I1IIII11I[int()]-12,I1IIII11I[int(not())]-10),10);
    if len(IIII11I11)==10:IIII11I11.pop(int());IIII11I11.append(I1IIII11I.copy());
    else:IIII11I11.append(I1IIII11I.copy());
    if len(III111II1)==10:III111II1.pop(int());III111II1.append(IIII11I11[int()]);
    else:III111II1.append(IIII11I11[int()]);
    if len(I11IIII1I)<IIII11I1I:I11IIII1I.append(list());
    if IIII11I1I>=int(not()):
        if len(I11IIII1I[int()])==10:I11IIII1I[int()].pop(int());I11IIII1I[int()].append(III111II1[int()]);
        else:I11IIII1I[int()].append(III111II1[int()]);
    if IIII11I1I>int(not()):
        for I1111111I in range(int(not()),IIII11I1I):
            if len(I11IIII1I[I1111111I])==10:I11IIII1I[I1111111I].pop(int());I11IIII1I[I1111111I].append(I11IIII1I[I1111111I-int(not())][int()]);
            else:I11IIII1I[I1111111I].append(I11IIII1I[I1111111I-int(not())][int()]);
    II1111II1.draw.circle(II1111I1I,(255,int(),int()),(IIII11I11[int()][int()],IIII11I11[int()][int(not())]),15);
    if IIII11I1I>=int(not()):II1111II1.draw.circle(II1111I1I,(255,int(),int()),(III111II1[int()][int()],III111II1[int()][int(not())]),15);
    if IIII11I1I>int(not()):
        for I1111111I in range(int(not()),IIII11I1I):
            II1111II1.draw.circle(II1111I1I,(255,int(),int()),(I11IIII1I[I1111111I-int(not())][int()][int()],I11IIII1I[I1111111I-int(not())][int()][int(not())]),15);
            I11I1111I=(abs(I11IIII1I[I1111111I-int(not())][int()][int()]-I1IIII11I[int()])**2+abs(I11IIII1I[I1111111I-int(not())][int()][int(not())]-I1IIII11I[int(not())])**2)**0.5;
            if I11I1111I<30:II11II11I=III11II11;
    if (I1IIII11I[int()]<10)or(I1IIII11I[int()]>sum(range(51))-5)or(I1IIII11I[int(not())]<10)or(I1IIII11I[int(not())]>sum(range(39))-31):II11II11I=III11II11;
    II1111II1.display.flip();I111II111.tick(60);
while III1III11==III1III11:
    for I1III11II in II1111II1.event.get():
        if I1III11II.type==II1111II1.QUIT:II1111II1.quit();exec(chr(113)+"u"+chr(105)+"t()");
    try:II1111I1I.blit(II1111II1.transform.scale(II1111II1.image.load('sdxfchgvnj dg  erdhd'+chr(33)+'!:;;s<g g.js.jpg'),(sum(range(51))+5,sum(range(39))-21)),(int(),)*2);II1111II1.display.flip();I111II111.tick(20);
    except:II1111I1I.blit(II1111II1.transform.scale(II1111II1.image.load('sdxfchgvnj dg  erdhd'+chr(33)+'!_;;s_g g.js.jpg'),(sum(range(51))+5,sum(range(39))-21)),(int(),)*2);II1111II1.display.flip();I111II111.tick(20);
