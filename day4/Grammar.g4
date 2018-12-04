grammar Grammar;


root : line+ EOF ;

line: LBR date RBR WS action NEWLINE ;

date : (year = NUMBER) DASH (month = NUMBER) DASH (day = NUMBER)
       WS
       (hour = NUMBER) COLON (minute = NUMBER);

action : 'falls asleep' # asleep
       | 'wakes up' # wakeup
       | 'Guard #' (guard = NUMBER) ' begins shift' # shift
       ;


RBR : ']' ;
COLON : ':' ;
LBR : '[' ;
DASH : '-' ;
NUMBER : [0-9]+ ;
NEWLINE : '\n' ;
WS : [\t ] ;