import sys
#hlias kakosimos 4066 kapsalis vasileios 4080
#cse74080 cse74066 
#lektikos analuths 
# =========================== #


# =========================== #

# lektikh monada
#lektikh monada pros suntaktiko analuth
#lektikh monada pinakas [sumvoloseira pou diavase,family,grammh1_number]
#family: 
#identifier onomata metavlitwn sunarthsewn diadikasiwn statherwn 
#keyword while if else klp
#id operaretor groupsymbos
#LEKTIKES MONADES

#GLOBAL VARIABLES 
global grammh1
global counter 
global run_again_times


global error_counter
global counter12 
grammh1 = 1
# =========================== #

#operator distribution
operator = ["+","-","*","/"]
rel_operator = ["<",">","=",]

#omadopoioume gia na ftiaxoume pinakes - oi pinakes tha thelame na einai me metavlhto megethos alla den mas ta evgaze swsta
#estw oti prepei na exoume stis grammes onomata pinakwn 
#pou apoteloun tis katastaseis omadopoihshs gia to aftomato 
exw_begin=0
exw_word_letter=1 
exw_number_digit=2

exw_less=3
exw_greater=4
exw_isothta=5
exw_hashtag=6
exw_comms = 7
exw_hashtag_close = 8

exw_div_diairesh=9

exw_thavmastiko=10

# =========================== #

####THETOUME TIS APARAITHTES METAVLHTES TOU KATHE PINAKA ME VASH TIS KATASTASEIS TOU KAI TON ARITHMO TOU
keno=0


grammata = 1

arithmoi = 2
plus=3

minus_something=4

multiply=5

divide=6

assign=7 # =

less_than=9

greater_than=9

eof_key = 10 # ;
not_found_reader_fileacter = 11
comma = 12

semilolomfound = 13 #: 

aristeri_par =14  #()
dexia_parentesh = 15

aggylh_kleise_2 = 16 # {} 

aggylh_anoixe_2 = 17

open_block = 18
close_block = 19

lin_change_now = 20

anwkatw_teleia= 21

hashtag = 22
dollar  = 23
quotes = 24
underscore = 25
exclamation_mark = 26


# =========================== #
# =========================== #

numbers = ['0','1','2','3','4','5','6','7','8','9']
#me grammata 
cutepy_sletters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
cutepy_cletters = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
cutepy_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f',
            'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

####ARXH LEKTIKWN MONADWN 
# =========================== #

#LEKTIKES MONADES CUTEPY ARITHMISH 
quotes_lm = 100
identifier_lm=101
afairesh_lm=1012
pollaplasiasmos_lm=1013
mikrotero_isso_lm=1014
comments_lm=1015
close_block_type2_lm=1016
open_block_type2_lm = 1017
anw_katw_teleia_lm= 1018
anathesi_mono_ison_lm=1019
diaforo_tou_lm=10110
megalutero_iso_lm= 10112
diairesh_lm=10113
komma_lm=10114
semicolom_lm=10115 #erwthmatiko ellhniko
anoigma_parenthesi_lm=10116
kleisimo_parenthesi_lm=10117
megalutero_apo_lm=10118
eof_key_lm=10119
arithmos_lm=10120
equal_diplo_iso_lm=10121
lessthan_lm=10122
prosthesi_lm=10123
open_aggules_listwn_lm=10124 
close_aggules_listwn_lm=10125

#ERROR SECTION OF CUTE PY
we_encountered_an_error_id_should_begin_with_underscore = 200
we_encountered_an_error_int_out_of_border = 201
we_encountered_an_error_int_before_letter = 202 
we_encountered_an_error_not_a_known_reader_fileacter = 203
we_encountered_an_error_opening_comment_section_and_not_closing = 204 
we_encountered_an_error_sign_dollar_cannot_be_used_in_this_order = 205
we_encountered_an_error_sign_slash_cannot_be_used_in_this_order = 206
we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order = 207
we_encountered_an_error_sign_right_list_opener_cannot_be_used_in_this_order = 222
we_encountered_an_error_sign_left_list_opener_cannot_be_used_in_this_order = 209
we_encountered_an_error_not_exclamation_mark_alone = 210 #should be paired
we_encountered_an_error_please_try_again = 211 #random error
we_encountered_an_error_string_out_of_bounds = 212
we_encountered_an_error_not_known_reader_fileacter = 213 #not known reader_fileacter error
we_encountered_an_Error_loading_the_application = 214
we_encountered_an_error_reliling = 215
we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order = 216
we_encountered_an_error_sign_left_curly_opener_cannot_be_used_in_this_order = 217


#Group of lektikes monades programmatos - 
#reserver word group
#prosthafaireseis group


cutepy_quotes_group = []
cutepy_reserved_group =['def' ,'#declare','if','else','while','return',
                    'and','or','not','input','print','int','__name__','__main__']

integer_lm=99933
name_lm=99944
main_lm=99955
def_lm=999
declare_lm=9992

and_lm=9997
or_lm=9998
not_lm=9999
input_lm=99911
print_lm=99922
if_lm=9993
else_lm=9994
while_lm=9995
return_lm=99956


##to motivo poy ftiaxame einai mia arxikh poy epanalamvanei kai an kati apo afta dwsei kapoio error h token paei ston pinaka katastashs poy tou armozei kai to pairnei
close_block_type2_lm=1016
open_block_type2_lm = 1017



dimensional_aftomato=[
        [exw_begin,exw_word_letter,exw_number_digit,prosthesi_lm,afairesh_lm,pollaplasiasmos_lm,exw_div_diairesh,
        exw_isothta,exw_less,exw_greater,eof_key_lm,we_encountered_an_error_not_known_reader_fileacter,komma_lm,
        semicolom_lm,anoigma_parenthesi_lm,kleisimo_parenthesi_lm,open_aggules_listwn_lm,close_aggules_listwn_lm,we_encountered_an_error_sign_left_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,exw_begin,anw_katw_teleia_lm,exw_hashtag,we_encountered_an_error_sign_dollar_cannot_be_used_in_this_order,
        quotes_lm,exw_word_letter,exw_thavmastiko],
        
    #exw_word_letter
        [identifier_lm,exw_word_letter,exw_word_letter,identifier_lm,identifier_lm,identifier_lm,identifier_lm,identifier_lm,identifier_lm,identifier_lm,identifier_lm,we_encountered_an_error_not_known_reader_fileacter,identifier_lm,identifier_lm,identifier_lm,identifier_lm,identifier_lm,identifier_lm,identifier_lm,identifier_lm,identifier_lm,identifier_lm,identifier_lm,identifier_lm,identifier_lm,exw_word_letter,identifier_lm],
        
    #exw_number_digit
        [arithmos_lm,we_encountered_an_error_int_before_letter, exw_number_digit,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,we_encountered_an_error_not_known_reader_fileacter,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm,arithmos_lm],

    #exw_less
    ##oles oi periptwseis petagontai sto less than lektikh monada ektos tou ison pou erxetai apo to exw_isothta ara sunexizei sto less than lektikhoi monada
        [lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,mikrotero_isso_lm,lessthan_lm,lessthan_lm,
        lessthan_lm,we_encountered_an_error_not_known_reader_fileacter,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm,lessthan_lm],

    #exw_greater
    ##same as 236
        [megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,
        megalutero_iso_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,we_encountered_an_error_not_known_reader_fileacter,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm,megalutero_apo_lm],

     #exw_isothta
        [anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,
        anathesi_mono_ison_lm,anathesi_mono_ison_lm,equal_diplo_iso_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,we_encountered_an_error_not_known_reader_fileacter,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm,anathesi_mono_ison_lm],

     #exw_hashtag
        [we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        exw_word_letter,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_not_known_reader_fileacter,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        open_block_type2_lm,
        close_block_type2_lm,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        exw_comms,we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order],

     #exw_comms
        [exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        we_encountered_an_error_opening_comment_section_and_not_closing,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms
        ,exw_comms,
        exw_hashtag_close,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms],

     #exw_hashtag_close
        [exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        we_encountered_an_error_opening_comment_section_and_not_closing,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_comms,
        exw_hashtag_close,
        exw_begin,
        exw_comms,
        exw_comms,
        exw_comms],

     #exw_div_diairesh
        [we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        diairesh_lm,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_not_known_reader_fileacter,we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order,
        we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order],

     #exw_thavmastiko
        [we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        diaforo_tou_lm,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_known_reader_fileacter,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone,
        we_encountered_an_error_not_exclamation_mark_alone]
        ]

if len(sys.argv) < 2:
    print("how to call programm - > python open_file.py <filename.cutePy>")
    sys.exit(1)
filename = sys.argv[1]


try:
    file = open(filename, 'r', encoding='utf8')
except FileNotFoundError:
    print(f"not found'{filename}'")
    sys.exit(1)


def lex():
        #not saving grammh1 coutner
        #saved
        global grammh1
        save_string=''
        #thetw  ekinhsh 0
        trexousa_katastash= exw_begin
        #SyntaxError: name 'grammh1' is used prior to global declaration?????????
        counter_lin_third= grammh1
        saved_output=[]
        ##print('this is what was given : ' ,dimensional_aftomato[trexousa_katastash][dexomeno_lm_twra])
        #print(breakpoint318)
        
        while(trexousa_katastash>=0 and trexousa_katastash<=10):
                reader_file = file.read(1)

                if (reader_file == ' '):
                        dexomeno_lm_twra = keno
                elif (reader_file == '\t'):
                        dexomeno_lm_twra = keno
                elif (reader_file in cutepy_letters):
                        dexomeno_lm_twra = grammata
                elif (reader_file == '/'):
                        dexomeno_lm_twra = divide
                elif(reader_file == '='):
                        dexomeno_lm_twra = assign
                elif (reader_file == '#'):
                        dexomeno_lm_twra = hashtag

                elif (reader_file == '$'):
                        dexomeno_lm_twra = dollar
                elif (reader_file == '<'):
                        dexomeno_lm_twra = less_than
                elif (reader_file == '>'):
                        dexomeno_lm_twra = greater_than
                elif (reader_file == ':'):
                        dexomeno_lm_twra = anwkatw_teleia
                elif (reader_file == ','):
                        dexomeno_lm_twra = comma
                elif (reader_file == '"'):
                        dexomeno_lm_twra = quotes
                elif (reader_file == '_'):
                        dexomeno_lm_twra = underscore
                elif (reader_file in numbers):
                        dexomeno_lm_twra = arithmoi
                elif (reader_file == '-'):
                        dexomeno_lm_twra = minus_something
                elif (reader_file == '+'):
                        dexomeno_lm_twra = plus
                elif (reader_file == '*'):
                         dexomeno_lm_twra = multiply
                elif (reader_file == '!'):
                        dexomeno_lm_twra = exclamation_mark
                elif (reader_file == '.'):
                        dexomeno_lm_twra = teleia
                elif (reader_file == ';'):
                        dexomeno_lm_twra = semilolomfound
                elif (reader_file == '('):
                        dexomeno_lm_twra = aristeri_par
                elif (reader_file == ')'):
                        dexomeno_lm_twra = dexia_parentesh
                elif (reader_file == '['):
                        dexomeno_lm_twra = aggylh_anoixe_2
                elif (reader_file == ']'):
                        dexomeno_lm_twra = aggylh_kleise_2
                elif (reader_file == '{'):
                        dexomeno_lm_twra = open_block
                elif (reader_file == '}'):
                        dexomeno_lm_twra = close_block
                elif (reader_file == '\n'):
                        counter_lin_third=counter_lin_third+1
                        dexomeno_lm_twra = lin_change_now
                elif (reader_file == ''):  #eof_key or ''
                        dexomeno_lm_twra = eof_key
                
                
                        
                #print(breakpoint383)
                
                else:
                        dexomeno_lm_twra = not_found_reader_fileacter



               # print('input pinaka 1 prin ', trexousa_katastash)
                #print('input pinaka 2 prin ', dexomeno_lm_twra)
                
                
                trexousa_katastash=dimensional_aftomato[trexousa_katastash][dexomeno_lm_twra]
                #print('input pinaka 1 ', trexousa_katastash)
                #print('input pinaka 2 ', dexomeno_lm_twra)
                #print('Nea katastasi ', trexousa_katastash)
                
                
                if(len(save_string)<30):
                        if(trexousa_katastash!=exw_begin and trexousa_katastash!=exw_comms and trexousa_katastash!=exw_hashtag_close):
                              save_string+=reader_file
                        else:
                              save_string=''

                else:
                        trexousa_katastash=we_encountered_an_error_int_out_of_border
                        #lektikh monada vrethike
        if(trexousa_katastash==identifier_lm or trexousa_katastash==arithmos_lm or trexousa_katastash==lessthan_lm or trexousa_katastash==megalutero_apo_lm or trexousa_katastash==anathesi_mono_ison_lm):

                 
                        if (reader_file == '\n'):
                               counter_lin_third -= 1
                               
                        reader_file=file.seek(file.tell()-1,0)  #opws sthn c , me lseek fseek gurizei to prohgoymeno stoixeio 
                        save_string = save_string[:-1]        #vgazei to teleftaio + gia nea katastash


        if(trexousa_katastash==identifier_lm):
                if(save_string in cutepy_reserved_group):
                        if(save_string=='def'):
                                trexousa_katastash=def_lm
                        elif(save_string=='#declare'):
                                trexousa_katastash=declare_lm
                        elif (save_string == 'if'):
                                trexousa_katastash = if_lm
                        elif (save_string == 'else'):
                                trexousa_katastash = else_lm
                        elif (save_string == 'while'):
                                trexousa_katastash = while_lm
                        elif (save_string == 'and'):
                                trexousa_katastash = and_lm
                        elif (save_string == 'or'):
                                trexousa_katastash = or_lm
                        elif (save_string == 'not'):
                                trexousa_katastash = not_lm
                        elif (save_string == 'input'):
                                trexousa_katastash = input_lm
                        elif (save_string == 'int'):
                                trexousa_katastash = integer_lm
                        elif (save_string == 'print'):
                                trexousa_katastash = print_lm
                        elif (save_string == 'return'):
                                trexousa_katastash = return_lm
                        elif (save_string == '__name__'):
                                trexousa_katastash = name_lm
                        elif (save_string == '__main__'):
                                trexousa_katastash = main_lm
                elif (save_string[0] == '_'):
                     trexousa_katastash=ERROR_ID_KSEKINA_ME_KATW_PAYLA


        
        
        correctinteger = 0

        
        if (trexousa_katastash == arithmos_lm):
                if(save_string.isdigit()):
                        num = int(save_string)
                        if -32766 <= num <= 32766:
                            correctinteger = 1
                        else:
                                trexousa_katastash==we_encountered_an_error_int_out_of_border
                                print("Twe_encountered_an_error_int_out_of_border.")
                                #print(breakpoint12)
        #ELEGXOS TWN ERRORS
        if(trexousa_katastash==we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order):
                print("we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order")
        elif(trexousa_katastash==we_encountered_an_error_not_exclamation_mark_alone):
                print("we_encountered_an_error_not_exclamation_mark_alone")
        elif(trexousa_katastash==we_encountered_an_error_not_known_reader_fileacter):
                print("we_encountered_an_error_not_known_reader_fileacter")
        elif(trexousa_katastash==we_encountered_an_error_int_out_of_border):
                print("we_encountered_an_error_int_out_of_border")
        elif(trexousa_katastash==we_encountered_an_error_int_out_of_border):
                print("we_encountered_an_error_int_out_of_border")
        elif(trexousa_katastash==we_encountered_an_error_sign_dollar_cannot_be_used_in_this_order):
                print("we_encountered_an_error_sign_dollar_cannot_be_used_in_this_order")


        if(trexousa_katastash==we_encountered_an_error_int_before_letter):
                print("we_encountered_an_error_int_before_letter")
        
        elif(trexousa_katastash==we_encountered_an_error_opening_comment_section_and_not_closing):
                print("we_encountered_an_error_opening_comment_section_and_not_closing")
        elif(trexousa_katastash==we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order):
                print("we_encountered_an_error_sign_right_curly_opener_cannot_be_used_in_this_order")
        elif(trexousa_katastash==we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order):
                print("we_encountered_an_error_sign_hashtag_cannot_be_used_in_this_order")
        elif(trexousa_katastash==we_encountered_an_error_sign_left_curly_opener_cannot_be_used_in_this_order):
                print("we_encountered_an_error_sign_left_curly_opener_cannot_be_used_in_this_order")
        elif(trexousa_katastash==we_encountered_an_error_id_should_begin_with_underscore):
                print("we_encountered_an_error_id_should_begin_with_underscore")
        



        #append1 lektikh moanda , append 2 to string, append3 to arithmo grammhs
        saved_output.append(trexousa_katastash)
        saved_output.append(save_string)
        saved_output.append(counter_lin_third) #oxi aparaithto
        grammh1=counter_lin_third

        #print(saved_output)
        #print(breakpoint12)
        return saved_output

# Endiamesos kodikas

global listOfAllQuads       #lista me all quads .
listOfAllQuads = []
countQuad = 1               #quad identifier front number
def nextQuad():
    #next number identifier of quad when generated
    global countQuad
    
    return countQuad

listOfAllQuadsFinal = []
def genQuad(first, second, third, fourth):
    #next quad generated 
    #identifier and quad after
    global countQuad
    global listOfAllQuads
    global listOfAllQuadsFinal
    list = []
    
    list = [nextQuad()]         #Bazw prwta ton arithmo.
    list += [first] + [second] + [third] + [fourth]     #Epeita ta orismata
    
    countQuad +=1   #next quad identifier +! 
    listOfAllQuads += [list]    #add to  global listOfAllQuads.
    listOfAllQuadsFinal += [list]   #xrhsimopoiasa thn final lista listOfAllQuadsFinal mhpws enwsw 
    return list

T_i = 1
listOfTempVariables = []
def newTemp():
    #temporarry metavlhtes T_1, T_2,.. .'
    global T_i
    global listOfTempVariables
    
    list = ['T_']
    list.append(str(T_i))
    tempVariable="".join(list)
    T_i +=1

    return tempVariable
def emptyList():
    #generated quad empty
    pointerList = []    
    
    return pointerList
def makeList(x):
    #mono to x mesa sthn lista 4adwn
    
    listThis = [x]
    
    return listThis
def merge(list1, list2):
    #lista poy kollaei tis tetrades list1 list2 
    list=[]
    list += list1 + list2

    return list
def backPatch(list, z):
    
    #list exei mesa deiktes se tetrades listofallquads twn opoiwn pou den einai sumplhrwmenes 
    # mpainei h etiketa apo to z me thn klhsh backpath kai tis gemizei
    #otan vriskei _ sto last 4digit tha kanei backpatch me z sthn thesh to



    global listOfAllQuads
    
    for i in range(len(list)):
        for j in range(len(listOfAllQuads)):
            if(list[i]==listOfAllQuads[j][0] and listOfAllQuads[j][4]=='_'):
                listOfAllQuads[j][4] = z
                break;
    return




#prospatheia pinaka sumbolwn den exei bei 

# class Argument():
#     def __init__(self):
#         self.name = ''
#         self.type = 'Int'

# class Entity():
#     def __init__(self, name):
#         self.variable = self.Variable()
#         self.subprogram = self.SubProgram()
#         self.subprogram - self.Procedure()
#         self.parameter = self.Parameter()
#         self.tempVar = self.TempVar()

#     class Variable(Entity):
#         def __init__(self, name, data_type, offset):
#             self.data_type = data_type
#             self.offset = offset

# class Procedure(Entity):
#     def __init__(self, name, parameters):
#         self.parameters = parameters

# class SubProgram:
#     def __init__(self, name, parameters, return_type, start_quad, framelength):
#         self.return_type = return_type
#         self.start_quad = start_quad
#         self.framelength = framelength
#         self.argumentList = []          #h lista parametrwn (gia na apothikeuso ta TRIGONA)
#         self.nestingLevel = 0       # gia ton teliko



# class Constant(Entity):
#     def __init__(self, name, value):
#         self.value = value

#     def get_type(self):
#         return "Constant"

# class Parameter:
#     def __init__(self, name, par_mode, offset):
#         self.par_mode = par_mode
#         self.offset = offset

#     def get_type(self):
#         return "Parameter"

# class TempVar:
#     def __init__(self, name, offset):
#         super().__init__(name)
#         self.offset = offset



# class Scope:
#     def __init__(self, nesting_level):
#         self.name = ''                      #Dinw to name gia na kserw poio Scope einai.
#         self.entities = []
#         self.nesting_level = nesting_level

# #vazw sto argument p dothike to subprogram me vash to scope 
# def new_argument(argument_object): 
#     global topScope
    
#     if topScope.entityList:
#         subprogram = topScope.entityList[-1]  # Get the last entity, which is a subprogram (function or procedure)
#         if isinstance(subprogram, Subprogram):
#             subprogram.argumentList.append(argument_object)

# def new_entity(entity_object):
#     global topScope
#     #vale sto entity object sthn lista me entities top scope
#     topScope.entityList.append(entity_object) 

# topScope = None     


# #  create a new scope 
# def new_scope(name):
#     global topScope

#     nextScope = Scope()   
#     nextScope.name = name
#     nextScope.enclosingScope = topScope

#     if topScope is None: 
#         nextScope.nestingLevel = 0
#     else:
#         nextScope.nestingLevel = topScope.nestingLevel + 1

#     topScope = nextScope


# #delete scope and its entities call
# def delete_scope(): 
    
#     global topScope
    
#     freeScope = topScope
#     topScope = topScope.enclosingScope
#     if freeScope.entityList:
#         for entity in freeScope.entityList:
#             del entity  






###arxh suntaktikou analuth



def syntax_analysis():
        global grammh1
        global lexres
        lexres= lex()
        grammh1 = lexres[2]



        #start of kanones
        def startRule():

            
            def_main_part()
            call_main_part()

        
        def def_main_part():
            global lexres
            
            def_main_function()
            while(lexres[0] == def_lm):
                 def_main_function()
        ##call the main checks error
        
        def def_main_function():
                global grammh1 
                global lexres
                
                
                if(lexres[0] == def_lm):
                        lexres = lex()
                        grammh1 = lexres[2]
                        
                        if(lexres[0] == identifier_lm):
                                name = lexres[1]
                                lexres = lex()
                                grammh1 = lexres[2]

                                if(lexres[0] == anoigma_parenthesi_lm):
                                        lexres = lex()
                                        grammh1 = lexres[2]
                        
                                        if(lexres[0] == kleisimo_parenthesi_lm):
                                                lexres = lex()
                                                grammh1 = lexres[2]
                                                
                                                if(lexres[0] == anw_katw_teleia_lm):
                                                      lexres = lex()
                                                      grammh1 = lexres[2]
                                
                                                      if lexres[0] == open_block_type2_lm:
                                                          lexres = lex()
                                                          grammh1 = lexres[2]
                                                          
                                                          
                                                          declarations()
                                                          #declarations()
                                                          while(lexres[0] == def_lm):
                                                              def_function()
                                                              
                                                              
                                                          
                                                          

                                                          genQuad('begin_block',name,'_','_')
                                                          
                                                          statements()
                                                          #relute_framelength()
                                                          genQuad('end_block',name,'_','_')
                                                          
                                                          if(lexres[0] == close_block_type2_lm):
                                                              lexres = lex()
                                                              grammh1 = lexres[2]
                                                          else:
                                                              print(" #} after main identifier not found +__+call from syntax_analysis",grammh1)
                                                              exit(-1)
                                                      else:
                                                           print("#{ declaration not relete+__+call from syntax_analysis ",grammh1)
                                                           exit(-1)
                                                else:
                                                      print("()after main sentence not found)+__+call from syntax_analysis",grammh1)
                                                      exit(-1)
                                        else:
                                                print("right parenthesis after main sentence+__+call from syntax_analysis",grammh1)
                                                exit(-1)
                                else:
                                        print("left parenthesis does not open correctly+__+call from syntax_analysis",grammh1)
                                        exit(-1)

                        else:
                                print("main identifier not foubd+__+call from syntax_analysis",grammh1)
                                exit(-1)
                else:
                         print("def identifier not found at start+__+call from syntax_analysis",grammh1)
                         exit(-1)
                        
        
        ##order of flow , elegxos meta apo kalesma function se cutepy pithana error                
        def def_function():
                global grammh1 
                global lexres
                
                if(lexres[0] == def_lm):
                        lexres = lex()
                        grammh1 = lexres[2]
                        
                        if(lexres[0] == identifier_lm):
                                name = lexres[1]
                                lexres = lex()
                                grammh1 = lexres[2]

                                if(lexres[0] == anoigma_parenthesi_lm):
                                        lexres = lex()
                                        grammh1 = lexres[2]
                                        
                                        id_list()
                        
                                        if(lexres[0] == kleisimo_parenthesi_lm):
                                                lexres = lex()
                                                grammh1 = lexres[2]
                                                
                                                if(lexres[0] == anw_katw_teleia_lm):
                                                      lexres = lex()
                                                      grammh1 = lexres[2]
                                
                                                      if(lexres[0] == open_block_type2_lm):
                                                          lexres = lex()
                                                          grammh1 = lexres[2]
                                                          

                                                          declarations()
                                                          
                                                          while(lexres[0] == def_lm):
                                                              def_function()
                                                              ##checked den doylepse me call
                                                          
                                                          
                                                          genQuad('begin_block',name,'_','_')

                                                          statements()
                                                          #relute_framelength()
                                                          genQuad('end_block',name,'_','_')
                                                          #print_Symbol_table()
                                                          
                                                          if(lexres[0] == close_block_type2_lm):
                                                              lexres = lex()
                                                              grammh1 = lexres[2]
                                                             
                                                          else:
                                                              print(" not found #} after statement+__+call from syntax_analysis ",grammh1)
                                                              exit(-1)
                                                      else:
                                                           print("not found #{ +__+call from syntax_analysis",grammh1)
                                                           exit(-1)
                                                else:
                                                      print("cannot find ()+__+call from syntax_analysis",grammh1)
                                                      exit(-1)
                                        else:
                                                print("right parenthesis after function name+__+call from syntax_analysis",grammh1)
                                                exit(-1)
                                else:
                                        print("left parenthesis after function name+__+call from syntax_analysis",grammh1)
                                        exit(-1)

                        else:
                                print("function name missing+__+call from syntax_analysis",grammh1)
                                exit(-1)
                else:
                         print("def noit found+__+call from syntax_analysis",grammh1)
                         exit(-1)

        def declarations():
            global lexres
            
            
            while(lexres[0] == declare_lm):
                 declaration_grammh1()

        def declaration_grammh1():
                global lexres 
                
                if (lexres[0] == declare_lm):
                        lexres = lex()
                        grammh1 = lexres[2]
                        
                        id_list()


              
        def id_list():
                global grammh1 
                global lexres
                #print('breakpoint857')
                if(lexres[0] == identifier_lm):
                        name = lexres[1]
                        lexres = lex()
                        grammh1 = lexres[2]
                        

                        

                        while(lexres[0] == komma_lm):
                                lexres = lex()
                                grammh1 = lexres[2]
                                
                                if(lexres[0] == identifier_lm):
                                        name = lexres[1]
                                        lexres = lex()
                                        grammh1 = lexres[2]
                                        
                                else:
                                        print("id after comma+__+call from syntax_analysis", grammh1)
                                        exit(-1)               
               
        
        def statement():
           global grammh1
           global lexres
           #print('breakpoint8773412')
           #print(lexres)
           if(lexres[0]==identifier_lm or lexres[0]==print_lm or lexres[0]==return_lm):
                #print('breakpoint8773')
                simple_statement()
           elif(lexres[0]==if_lm or lexres[0]==while_lm):
                #print('breakpoint87733')
                structured_statement()
           else:
                print("lathos den", grammh1)
                exit(-1)
                

        def statements():
           global lexres

           statement()
           while(lexres[0]==identifier_lm or lexres[0]==print_lm or lexres[0]==return_lm or lexres[0]==if_lm or lexres[0]==while_lm):
                statement()

        def simple_statement():
           global lexres
           
           if(lexres[0]==identifier_lm):
                assignment_stat()
           elif(lexres[0]==print_lm):
                print_stat()
           elif(lexres[0]==return_lm):
                return_stat()
        
        def structured_statement():
           global lexres
           if(lexres[0]==if_lm):
                ifStat()
           elif(lexres[0]==while_lm):
                whileStat()

        def assignment_stat():
                global lexres
                global grammh1
                if(lexres[0] == identifier_lm):
                        myid = lexres[1]
                        lexres = lex()
                        grammh1 = lexres[2]
                        
                        if(lexres[0] == anathesi_mono_ison_lm):
                                lexres = lex()
                                grammh1 = lexres[2]
                                
                                if(lexres[0] == integer_lm):
                                    lexres = lex()
                                    grammh1 = lexres[2]
                                    genQuad('inp',myid,'_','_')
                                    if(lexres[0] == anoigma_parenthesi_lm):
                                        lexres = lex()
                                        grammh1 = lexres[2]

                                        if(lexres[0] == input_lm):
                                            lexres = lex()
                                            grammh1 = lexres[2]

                                            if(lexres[0] == anoigma_parenthesi_lm):
                                                 lexres = lex()
                                                 grammh1 = lexres[2]
                                                
                                                 if(lexres[0] == kleisimo_parenthesi_lm):
                                                      lexres = lex()
                                                      grammh1 = lexres[2]
                                
                                                      if(lexres[0] == kleisimo_parenthesi_lm):
                                                          lexres = lex()
                                                          grammh1 = lexres[2]
                                                          
                                                          
                                                          if(lexres[0] == semicolom_lm):
                                                              lexres = lex()
                                                              grammh1 = lexres[2]
                                                          else:
                                                              print("semicolum missing+__+call from syntax_analysis",grammh1)
                                                              exit(-1)
                                                      else:
                                                           print("missing ) at assign stat+__+call from syntax_analysis",grammh1)
                                                           exit(-1)
                                                 else:
                                                      print("missing () at assign stat+__+call from syntax_analysis",grammh1)
                                                      exit(-1)
                                            else:
                                                      print("missing ) at assign stat+__+call from syntax_analysis",grammh1)
                                                      exit(-1)
                                        else:
                                                print("missing input at assign stat+__+call from syntax_analysis",grammh1)
                                                exit(-1)
                                    else:
                                           print("missing ( at assign stat+__+call from syntax_analysis",grammh1)
                                           exit(-1)
                                
                                else:
                                    Eplace = expression()
                                    genQuad(':=', Eplace, '_', myid)
                                    
                                    
                                
                                    if(lexres[0] == semicolom_lm):
                                        lexres = lex()
                                        grammh1 = lexres[2]
                                    else:
                                        print("missing semicolm at assign stat +__+call from syntax_analysis",grammh1)
                                        exit(-1)

                        else:
                                print("missing = after id +__+call from syntax_analysis.", grammh1)
                                exit(-1) 
                else:
                        print("missing id +__+call from syntax_analysis",grammh1)
                        exit(-1)
        def print_stat():
                global lexres
                global grammh1
                
                if(lexres[0] == print_lm):
                        lexres = lex()
                        grammh1 = lexres[2]

                        if(lexres[0] == anoigma_parenthesi_lm):
                                lexres = lex()
                                grammh1 = lexres[2]
                                
                                Eplace = expression()
                                genQuad('out', Eplace, '_', '_')
                                
                                
                                
                                if(lexres[0] == kleisimo_parenthesi_lm):
                                        lexres = lex()
                                        grammh1 = lexres[2]
                                        
                                        if(lexres[0] == semicolom_lm):
                                            lexres = lex()
                                            grammh1 = lexres[2]
                                        else:
                                            print("; after print_stat+__+call from syntax_analysis",grammh1)
                                            exit(-1)
                                else:
                                        print("missing ) after print_stat+__+call from syntax_analysis",grammh1)
                                        exit(-1)
                        else:
                                print("missing ( at ) print_stat+__+call from syntax_analysis", grammh1)
                                exit(-1)

                else:
                        print("no print+__+call from syntax_analysis",grammh1)
                        exit(-1)





        def return_stat():
                global lexres
                global grammh1
                
                if(lexres[0] == return_lm):
                        lexres = lex()
                        grammh1 = lexres[2]

                        if(lexres[0] == anoigma_parenthesi_lm):
                                lexres = lex()
                                grammh1 = lexres[2]
                                Eplace = expression()
                                genQuad('retv', Eplace, '_', '_')
                                
                                
                                
                                if(lexres[0] == kleisimo_parenthesi_lm):
                                        lexres = lex()
                                        grammh1 = lexres[2]
                                        
                                        if(lexres[0] == semicolom_lm):
                                            lexres = lex()
                                            grammh1 = lexres[2]
                                        else:
                                            print("return missing ; +__+call from syntax_analysis+__+call from syntax_analysis",grammh1)
                                            exit(-1)
                                else:
                                        print("missing ) return_stat+__+call from syntax_analysis",grammh1)
                                        exit(-1)
                        else:
                                print("missing ( return_stat+__+call from syntax_analysis", grammh1)
                                exit(-1)

                else:
                        print("missing return+__+call from syntax_analysis",grammh1)
                        exit(-1)

        #checked 231
        #psaxnw if 
        def ifStat():
                global lexres
                global grammh1
                
                if(lexres[0] == if_lm):
                        lexres= lex()
                        grammh1 = lexres[2]
                        
                        if(lexres[0] == anoigma_parenthesi_lm):
                                lexres = lex()
                                grammh1 = lexres[2]
                                
                                C = condition()
                                backPatch(C[0], nextQuad())
                                
                                if(lexres[0]== kleisimo_parenthesi_lm):
                                        lexres = lex()
                                        grammh1 = lexres[2]

                                        if(lexres[0] == anw_katw_teleia_lm):
                                             lexres = lex()
                                             grammh1 = lexres[2]
                                             
                                             if(lexres[0] == open_block_type2_lm):
                                                    lexres = lex()
                                                    grammh1 = lexres[2]

                                                    statements()
                                                    ifList = makeList(nextQuad())
                                                    genQuad('jump', '_', '_', '_')
                                                    backPatch(C[1], nextQuad())
                                                    if(lexres[0] == close_block_type2_lm):
                                                        lexres = lex()
                                                        grammh1 = lexres[2]
                                                    else:
                                                        print("  #}    not fount at+__+call from syntax_analysis ",grammh1)
                                                        exit(-1)
                                             else:
                                                    statement()
                                                    ifList = makeList(nextQuad())
                                                    genQuad('jump', '_', '_', '_')
                                                    backPatch(C[1], nextQuad())

                                                    
                                             if(lexres[0] == else_lm):
                                                lexres = lex()
                                                grammh1 = lexres[2]
                                             
                                                if(lexres[0] == anw_katw_teleia_lm):
                                                    lexres = lex()
                                                    grammh1 = lexres[2]
                                                    
                                                    if(lexres[0] == open_block_type2_lm):
                                                          lexres = lex()
                                                          grammh1 = lexres[2]
                                                    
                                                          statements()
                                                          
                                                          backPatch(ifList, nextQuad())
                                                          if(lexres[0] == close_block_type2_lm):
                                                              lexres = lex()
                                                              grammh1 = lexres[2]
                                                          else:
                                                              print("missin #} at  if+__+call from syntax_analysis",grammh1)
                                                              exit(-1)
                                                    else:
                                                          statement()
                                                          backPatch(ifList, nextQuad())

                                                else:
                                                    print("missing : at else +__+call from syntax_analysis",grammh1)
                                                    exit(-1)

                                        else:
                                            backPatch(ifList, nextQuad())
                                            print(" backpath called? 1659 missing : at if+__+call from syntax_analysis",grammh1)
                                              

                                else:
                                        print("missing ) if+__+call from syntax_analysis", grammh1)
                                        exit(-1)
                        else:
                                print(") missing at if+__+call from syntax_analysis", grammh1)
                                exit(-1)
                else:
                        print("missing if+__+call from syntax_analysis",grammh1)
                        exit(-1)
                

        def whileStat():
                global lexres
                global grammh1
                #print('breakpoint1155')
                if(lexres[0] == while_lm):
                        lexres= lex()
                        grammh1 = lexres[2]
                        
                        if(lexres[0] == anoigma_parenthesi_lm):
                                lexres = lex()
                                grammh1 = lexres[2]
                                
                                Cquad=nextQuad()
                                C = condition()
                                backPatch(C[0], nextQuad())
                                
                                if(lexres[0]== kleisimo_parenthesi_lm):
                                        lexres = lex()
                                        grammh1 = lexres[2]

                                        if(lexres[0] == anw_katw_teleia_lm):
                                             lexres = lex()
                                             grammh1 = lexres[2]
                                             
                                             if(lexres[0] == open_block_type2_lm):
                                                    lexres = lex()
                                                    grammh1 = lexres[2]
                                                    
                                                    statements()

                                                    genQuad('jump', '_', '_', Cquad)
                                                    backPatch(C[1], nextQuad())
                                                    
                                                    if(lexres[0] == close_block_type2_lm):
                                                        lexres = lex()
                                                        grammh1 = lexres[2]
                                                    else:
                                                        print("#} missing while+__+call from syntax_analysis",grammh1)
                                                        exit(-1)
                                             else:
                                                    statement()
                                                    ##jump checked
                                                    genQuad('jump', '_', '_', Cquad)
                                                    backPatch(C[1], nextQuad())
                                                    

                                        else:
                                              print(": missing at while +__+call from syntax_analysis",grammh1)
                                              exit(-1)

                                else:
                                        print("missing ) after while+__+call from syntax_analysis", grammh1)
                                        exit(-1)
                        else:
                                print("missing ( before while+__+call from syntax_analysis", grammh1)
                                exit(-1)
                else:
                        print("missing while while+__+call from syntax_analysis",grammh1)
                        exit(-1)

        def expression():
                global lexres
                global grammh1
                #print('breakpoint61206')
                optional_sign()
                T1place = term()

                while(lexres[0]==prosthesi_lm or lexres[0]==afairesh_lm):
                        plusOrMinus = ADD_OP()
                        T2place = term()

                        w = newTemp()
                        genQuad(plusOrMinus, T1place, T2place, w)
                        T1place = w
                        
                Eplace = T1place
                return Eplace
        

        def term():
                global lexres
                global grammh1
                
                F1place = factor()
                
                while(lexres[0]==pollaplasiasmos_lm or lexres[0]==diairesh_lm):
                        mulOrDiv = MUL_OP()
                        F2place = factor()

                        w=newTemp()
                        genQuad(mulOrDiv, F1place, F2place, w)
                        F1place = w

                Tplace =F1place
                return Tplace

                
            #checked 5   
        def factor():
                global lexres
                global grammh1
                #print('breakpoint1229')
                if(lexres[0]==arithmos_lm):
                        fact = lexres[1]
                        lexres = lex()
                        grammh1 = lexres[2]
                        
                elif(lexres[0]==anoigma_parenthesi_lm):
                        lexres = lex()
                        grammh1 = lexres[2]

                        Eplace = expression()
                        fact = Eplace
                        
                        
                        if(lexres[0]==kleisimo_parenthesi_lm):
                                lexres = lex()
                                grammh1 = lexres[2]
                        else:
                                print("missing )_ after factor call +__+call from syntax_analysis ",grammh1)
                                exit(-1)

                elif(lexres[0]==identifier_lm):
                        fact_temp = lexres[1]
                        lexres = lex()
                        grammh1 = lexres[2]
                        
                        fact = idtail(fact_temp)
                        
                else:
                    ##not working check
                        print("missing constant at variable by factor+__+call from syntax_analysis ",grammh1)
                        exit(-1)
                return fact
        #checked 4
        ##--------------------------------------------------------edw
        ##calling quads idtail
        def idtail(name):
                global lexres
                global grammh1
                
                if(lexres[0] == anoigma_parenthesi_lm ):
                        lexres = lex()
                        grammh1 = lexres[2]

                        actual_par_list()
                        w=newTemp()
                        genQuad('par', w, 'RET', '_')
                        genQuad('call', name, '_', '_')
                        ##defined above newTemp 
                        
                        
                        if(lexres[0]==kleisimo_parenthesi_lm):
                                lexres = lex()
                                grammh1 = lexres[2]
                                return w
                else:
                    return name
                        
        #checked 3                         
        def actual_par_list():
                global lexres
                global grammh1 
                
                if (lexres[0]==arithmos_lm or lexres[0]==anoigma_parenthesi_lm or lexres[0]==identifier_lm):
                    
                    Eplace1=expression()
                    genQuad('par', Eplace1, 'CV', '_')
                    
                    
                    while(lexres[0] == komma_lm):
                        lexres  = lex()
                        grammh1 = lexres[2]
                        
                        Eplace1=expression()
                        genQuad('par', Eplace1, 'CV', '_')
                
                        

        def optional_sign():
                global lexres
                global grammh1
                
                if(lexres[0] == prosthesi_lm or lexres[0] == afairesh_lm):
                        
                        ADD_OP()
        #checked 3 
        def ADD_OP():
                global lexres 
                global grammh1
                
                if(lexres[0]==prosthesi_lm):

                        lexres = lex()
                        grammh1 = lexres[2]
                        
                elif(lexres[0]==afairesh_lm):
                        lexres = lex()
                        grammh1 = lexres[2]


        #checked 3                
        def MUL_OP():
                global lexres 
                global grammh1
                
                if (lexres[0] == pollaplasiasmos_lm):

                        lexres = lex()
                        grammh1 = lexres[2]
                        
                elif (lexres[0] == diairesh_lm):

                        lexres = lex() #kalesma meta xana lektiko gia grammh 1 na valw metavlhth

                        grammh1 = lexres[2]


         ##checked 3        
        def condition(): ##sunarthsh if -> poy epistrefei 1 tetrada an einai true an einai false 
            #ctrue ckai cfalse antistoixa
                global lexres
                global grammh1
                BTtrue = []
                BTfalse = []
                
                Q1 = bool_term()

                BTtrue = Q1[0]
                BTfalse = Q1[1]
                
                while(lexres[0]==or_lm):
                        lexres=lex()
                        grammh1 = lexres[2]
                        backPatch(BTfalse, nextQuad())

                        Q2 = bool_term()
                        BTtrue = merge(BTtrue, Q2[0])
                        BTfalse = Q2[1]

                return BTtrue, BTfalse
                
                
        #checked 2
        def bool_term():
                global lexres
                global grammh1
                BTtrue = []
                BTfalse = []                
                
                Q1 = bool_factor()

                BTtrue = Q1[0]
                BTfalse = Q1[1]
                
                while lexres[0]==and_lm:
                        lexres=lex()
                        grammh1 = lexres[2]
                        backPatch(BTfalse, nextQuad())

                        Q2 = bool_factor()
                        BTtrue = merge(BTtrue, Q2[0])
                        BTfalse = Q2[1]

                return BTtrue, BTfalse

        ##checked 1
        def bool_factor():
                global lexres
                global grammh1
                BTtrue = []
                BTfalse = []
                
                if(lexres[0]==not_lm):
                        lexres=lex()
                        grammh1 = lexres[2]
                        
                        if(lexres[0]==close_aggules_listwn_lm):
                                lexres = lex()
                                grammh1 = lexres[2]
                                
                                Q = condition() ##dhlwsh condition endiamesou
                                
                                if(lexres[0]==close_aggules_listwn_lm):
                                        lexres = lex()
                                        grammh1 = lexres[2]
                                        BTtrue = Q[1]
                                        BTfalse = Q[0]

                                        
                                else:
                                        print("missing [ at bool factor] +__+call from syntax_analysis",grammh1)
                                        exit(-1)
                        else:
                                print("missing [ at bool facto]+__+call from syntax_analysis", grammh1)
                                exit(-1)

                elif(lexres[0]==close_aggules_listwn_lm):
                        lexres = lex()
                        grammh1 = lexres[2]
                        
                        Q = condition()
                        
                        if(lexres[0]==close_aggules_listwn_lm):
                                lexres = lex()
                                grammh1 = lexres[2]
                                BTtrue = Q[0]
                                BTfalse = Q[1]
                                

                                
                        else:
                                print("missing ] at bool_factor+__+call from syntax_analysis", grammh1)
                                exit(-1)
                else:
                        Eplace1 = expression()
                        
                        rel = REL_OP()
                        Eplace2 = expression()

                        BTtrue = makeList(nextQuad())
                        genQuad(rel, Eplace1, Eplace2, '_')
                        BTfalse = makeList(nextQuad())
                        genQuad('jump', '_', '_', '_')
                return BTtrue, BTfalse
                        
                        
                        
                         

        def REL_OP():
                global lexres 
                global grammh1
                
                if(lexres[0]==equal_diplo_iso_lm):
                        rel = lexres[1]
                        lexres = lex()
                        grammh1 = lexres[2]
                        
                elif(lexres[0]==lessthan_lm):
                        rel = lexres[1]
                        lexres = lex()
                        grammh1 = lexres[2]
                elif(lexres[0]== megalutero_apo_lm):
                        rel = lexres[1]
                        lexres = lex()
                        grammh1 = lexres[2]
                        
                elif(lexres[0]==megalutero_iso_lm):
                        rel = lexres[1]
                        lexres = lex()
                        grammh1 = lexres[2]        
                elif(lexres[0]==mikrotero_isso_lm):
                        rel = lexres[1]
                        lexres = lex()
                        grammh1 = lexres[2]
                        
                elif(lexres[0]==diaforo_tou_lm):
                        rel = lexres[1]
                        lexres = lex()
                        grammh1 = lexres[2]
                        
                
                        
                else:
                        print("missing math size operators +__+call from syntax_analysis",grammh1)
                        exit(-1)
                return rel

        def call_main_part():
                global lexres 
                global grammh1

                if(lexres[0] == if_lm):
                        lexres = lex()
                        grammh1 = lexres[2]
                        
                        if(lexres[0] == name_lm):
                                lexres = lex()
                                grammh1 = lexres[2]

                                if(lexres[0] == equal_diplo_iso_lm):
                                        lexres = lex()
                                        grammh1 = lexres[2]
                        
                                        if(lexres[0] == quotes_lm):
                                                lexres = lex()
                                                grammh1 = lexres[2]

                                                if(lexres[0] == main_lm):
                                                    lexres = lex()
                                                    grammh1 = lexres[2]

                                                    if(lexres[0] == quotes_lm):
                                                            lexres = lex()
                                                            grammh1 = lexres[2]
                                                
                                                            if(lexres[0] == anw_katw_teleia_lm):
                                                                lexres = lex()
                                                                grammh1 = lexres[2]

                                                                genQuad('begin_block', 'main', '_', '_')
                                                                main_function_call()
                                                                while(lexres[0] == identifier_lm):
                                                                     main_function_call()
                                                            else:
                                                                print("missing : n call_main_part +__+call from syntax_analysis",grammh1)
                                                                exit(-1)
                                                    else:
                                                        print("mising quotes call_main_part +__+call from syntax_analysis",grammh1)
                                                        exit(-1)
                                                else:
                                                   print("missing main call+__+call from syntax_analysis",grammh1)
                                                   exit(-1)
                                        else:
                                            print("missing quote at t call_main_part +__+call from syntax_analysis",grammh1)
                                            exit(-1)
                                else:
                                        print("missing assign at stin call_main_part +__+call from syntax_analysis",grammh1)
                                        exit(-1)

                        else:
                                print("missing name at call_main_part +__+call from syntax_analysis",grammh1)
                                exit(-1)
                else:
                         print("missing if at  call_main_part +__+call from syntax_analysis",grammh1)
                         exit(-1)
        
        def main_function_call():
                global grammh1 
                global lexres
                
                if(lexres[0] == identifier_lm):
                    genQuad('call', lexres[1], '_', '_')
                    lexres = lex()
                    grammh1 = lexres[2]

                    if(lexres[0] == anoigma_parenthesi_lm):
                        lexres = lex()
                        grammh1 = lexres[2]
                        
                        if(lexres[0] == kleisimo_parenthesi_lm):
                                lexres = lex()
                                grammh1 = lexres[2]
                                                
                                if(lexres[0] == semicolom_lm):
                                    lexres = lex()
                                    grammh1 = lexres[2]
                                
                                else:
                                    print("ERROR: Den yparxei ; stin main_function_call+__+call from syntax_analysis",grammh1)
                                    exit(-1)
                        else:
                            print("ERROR: Den kleinei h deksia parenthesi stin main_function_call+__+call from syntax_analysis",grammh1)
                            exit(-1)
                    else:
                        print("left ( at main_function_call+__+call from syntax_analysis",grammh1)
                        exit(-1)

                else:
                    print("missing id main_function_call+__+call from syntax_analysis",grammh1)
                    exit(-1)
        startRule()

syntax_analysis()

def print_listOfAllQuads():
        for i in range(len(listOfAllQuads)):
                print(str(listOfAllQuads[i][0])+" "+str(listOfAllQuads[i][1])+" "+str(listOfAllQuads[i][2])+" "+str(listOfAllQuads[i][3])+" "+str(listOfAllQuads[i][4]))

print_listOfAllQuads()
       
print('full run')
#print int file after succes run 
def intCode(intF):
    'Write listOfAllQuads at intFile.int'
    for i in range(len(listOfAllQuadsFinal)):
        quad = listOfAllQuadsFinal[i]
        intF.write(str(quad[0]))
        intF.write(" ")
        intF.write(str(quad[1]))
        intF.write(" ")
        intF.write(str(quad[2]))
        intF.write(" ")
        intF.write(str(quad[3]))
        intF.write(" ")
        intF.write(str(quad[4]))
        intF.write("\n")

intFile = open('intFile.int', 'w')
#endiamesos
intCode(intFile)

intFile.close()

ReadF = open('intFile.int', 'r')

final = open('final.asm', 'w')

#telikos kwdikas 


#mporw na valw kai ta up apo suntaktiko 
rel = ['=', '<=', '>=', '>', '<', '<>']

while(1):
        
        grammh1 = ReadF.readline()
        if not grammh1:
                break
        grammh1 = grammh1[:-1]
        grammh1 =grammh1.split(' ')

        if grammh1[1] == 'jump':
                temp_grammh1 = '\tb '+grammh1[4]+'\n'
                number = 'L'+grammh1[0]+':'+'\n'
                final.write(number)
                final.write(temp_grammh1)

        #rel search and branching 
        elif grammh1[1] in rel:
                if grammh1[1]=='=':
                        branch='beq'
                elif grammh1[1]=='<':
                        branch='blt'
                elif grammh1[1]=='>':
                    branch='bgt'
                elif grammh1[1]=='<=':
                    branch='ble'
                elif grammh1[1]=='>=':
                    branch='bge'
                else:
                    branch='bne'
                temp_grammh1='\tloadvr('+grammh1[2]+',t1)\n\tloadvr('+grammh1[2]+',t2)\n\t'+branch+',t1,t2,'+grammh1[4]+'\n'
                number='L'+grammh1[0]+':'+'\n'
                final.write(number)
                final.write(temp_grammh1) 

        #assignments load ad store
        elif grammh1[1]==':=':
                temp_grammh1='\tloadvr('+grammh1[2]+', t1)\n\tstorerv(t1,'+grammh1[4]+')'+'\n'
                number='L'+grammh1[0]+':'+'\n'
                final.write(number)
                final.write(temp_grammh1)

        #operator changeS
        elif grammh1[1] in operator:
                if grammh1[1]=='+':
                    op='add'
                elif grammh1[1]=='-':
                    op='sub'
                elif grammh1[1]=='*':
                    op='mul'
                elif grammh1[1]=='/':
                    op='div'
                temp_grammh1='\tloadvr('+grammh1[2]+', t1)\n\tloadvr(,'+grammh1[3]+',t2)\n\t'+op+'t1,t1,t2\nstorerv(t1,'+grammh1[4]+')'+'\n'
                number='L'+grammh1[0]+':'+'\n'
                final.write(number)
                final.write(temp_grammh1)

        #out load value ouut port 
        elif grammh1[1]=='out':
                temp_grammh1='\tli v0,1\n\tloadvr('+grammh1[4]+',a0)\n\tecall'+'\n'
                number='L'+grammh1[0]+':'+'\n'
                final.write(number)
                final.write(temp_grammh1)

        #in read data store value 
        elif grammh1[1]=='inp':
                temp_grammh1='\tli v0,5\n\tecall\n\tstorerv(v0,'+grammh1[4]+')'+'\n'
                number='L'+grammh1[0]+':'+'\n'
                final.write(number)
                final.write(temp_grammh1)

        #retv return value with load 
        elif grammh1[1]=='retv':
                temp_grammh1='\tloadvr('+grammh1[4]+', t1)\n\tlw t0,-8(sp)\n\tsw t1,(t0)'+'\n'
                number='L'+grammh1[0]+':'+'\n'
                final.write(number)
                final.write(temp_grammh1)

        #par parameter and method its called cb return value ,, klp
        elif grammh1[1]=='par':
                if grammh1[3]=='CV':
                    temp_grammh1='\tloadvr('+grammh1[2]+', t0)\n\tsw t0, -(12+4i)(fp)'+'\n'
                    number='L'+grammh1[0]+':'+'\n'
                    final.write(number)
                    final.write(temp_grammh1)
                elif grammh1[3]=='RET':
                    temp_grammh1='\tgnlvcode('+grammh1[2]+')\n\tlw t0,(t0)\n\tsw t0, -(12+4i)(fp)'+'\n'
                    number='L'+grammh1[0]+':'+'\n'
                    final.write(number)
                    final.write(temp_grammh1)
                else:
                    temp_grammh1='\taddi t0,sp,-offset\n\tsw t0,-8(fp)'+'\n'
                    number='L'+grammh1[0]+':'+'\n'
                    final.write(number)
                    final.write(temp_grammh1)

        #call
        elif grammh1[1]=='call':
                temp_grammh1='\tlw t0,-4(sp)\n\tsw t0,-4(fp)'+'\n'
                number='L'+grammh1[0]+':'+'\n'
                final.write(number)
                final.write(temp_grammh1)
        else:
                continue

final.close()
ReadF.close()

