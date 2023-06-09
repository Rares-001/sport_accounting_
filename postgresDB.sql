PGDMP     %                    {           sport_accounting    15.2    15.2 T    i           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            j           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            k           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            l           1262    16398    sport_accounting    DATABASE     r   CREATE DATABASE sport_accounting WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
     DROP DATABASE sport_accounting;
                postgres    false            �            1259    16621    accounting_module    TABLE     y   CREATE TABLE public.accounting_module (
    moduleid integer NOT NULL,
    module_name character varying(50) NOT NULL
);
 %   DROP TABLE public.accounting_module;
       public         heap    postgres    false            �            1259    16620    accounting_module_moduleid_seq    SEQUENCE     �   CREATE SEQUENCE public.accounting_module_moduleid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.accounting_module_moduleid_seq;
       public          postgres    false    215            m           0    0    accounting_module_moduleid_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.accounting_module_moduleid_seq OWNED BY public.accounting_module.moduleid;
          public          postgres    false    214            �            1259    16706    admin    TABLE     �   CREATE TABLE public.admin (
    adminid integer NOT NULL,
    firstname character varying(255) NOT NULL,
    lastname character varying(255) NOT NULL,
    email character varying(100) NOT NULL,
    password_ character varying(255) NOT NULL
);
    DROP TABLE public.admin;
       public         heap    postgres    false            �            1259    16705    admin_adminid_seq    SEQUENCE     �   CREATE SEQUENCE public.admin_adminid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.admin_adminid_seq;
       public          postgres    false    229            n           0    0    admin_adminid_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.admin_adminid_seq OWNED BY public.admin.adminid;
          public          postgres    false    228            �            1259    16628    bank    TABLE     �   CREATE TABLE public.bank (
    bankid integer NOT NULL,
    bank_name character varying(255) NOT NULL,
    banklocation character varying(255) NOT NULL
);
    DROP TABLE public.bank;
       public         heap    postgres    false            �            1259    16627    bank_bankid_seq    SEQUENCE     �   CREATE SEQUENCE public.bank_bankid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.bank_bankid_seq;
       public          postgres    false    217            o           0    0    bank_bankid_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.bank_bankid_seq OWNED BY public.bank.bankid;
          public          postgres    false    216            �            1259    16677    bar    TABLE     �   CREATE TABLE public.bar (
    barid integer NOT NULL,
    bar_name character varying(50) NOT NULL,
    moduleid integer NOT NULL
);
    DROP TABLE public.bar;
       public         heap    postgres    false            �            1259    16676    bar_barid_seq    SEQUENCE     �   CREATE SEQUENCE public.bar_barid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.bar_barid_seq;
       public          postgres    false    225            p           0    0    bar_barid_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.bar_barid_seq OWNED BY public.bar.barid;
          public          postgres    false    224            �            1259    16665    category    TABLE     �   CREATE TABLE public.category (
    categoryid integer NOT NULL,
    category_name character varying(50) NOT NULL,
    moduleid integer NOT NULL
);
    DROP TABLE public.category;
       public         heap    postgres    false            �            1259    16664    category_categoryid_seq    SEQUENCE     �   CREATE SEQUENCE public.category_categoryid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.category_categoryid_seq;
       public          postgres    false    223            q           0    0    category_categoryid_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.category_categoryid_seq OWNED BY public.category.categoryid;
          public          postgres    false    222            �            1259    16637    club    TABLE     B  CREATE TABLE public.club (
    clubid integer NOT NULL,
    clubname character varying(50) NOT NULL,
    club_address character varying(100) NOT NULL,
    club_city character varying(50) NOT NULL,
    club_phone character varying(20) NOT NULL,
    club_email character varying(50) NOT NULL,
    bankid integer NOT NULL
);
    DROP TABLE public.club;
       public         heap    postgres    false            �            1259    16636    club_clubid_seq    SEQUENCE     �   CREATE SEQUENCE public.club_clubid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.club_clubid_seq;
       public          postgres    false    219            r           0    0    club_clubid_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.club_clubid_seq OWNED BY public.club.clubid;
          public          postgres    false    218            �            1259    16649    customer    TABLE     �  CREATE TABLE public.customer (
    customer_id integer NOT NULL,
    username character varying(50) NOT NULL,
    password_ character varying(100) NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    email character varying(100) NOT NULL,
    phone_number character varying(20) NOT NULL,
    address character varying(200) NOT NULL,
    clubid integer NOT NULL
);
    DROP TABLE public.customer;
       public         heap    postgres    false            �            1259    16648    customer_customerid_seq    SEQUENCE     �   CREATE SEQUENCE public.customer_customerid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.customer_customerid_seq;
       public          postgres    false    221            s           0    0    customer_customerid_seq    SEQUENCE OWNED BY     T   ALTER SEQUENCE public.customer_customerid_seq OWNED BY public.customer.customer_id;
          public          postgres    false    220            �            1259    16739 
   mt940_file    TABLE     Z  CREATE TABLE public.mt940_file (
    mt940_id integer NOT NULL,
    status character(1),
    funds_code character varying(255),
    amount numeric(10,2),
    id character varying(255),
    customer_reference character varying(255),
    bank_reference character varying(255),
    extra_details character varying(255),
    currency character varying(10),
    date date,
    entry_date date,
    guessed_entry_date date,
    transaction_details text,
    final_closing_balance numeric(10,2),
    final_closing_balance_currency character varying(10),
    final_closing_balance_date date,
    available_balance numeric(10,2),
    available_balance_currency character varying(10),
    available_balance_date date,
    forward_available_balance numeric(10,2),
    forward_available_balance_currency character varying(10),
    forward_available_balance_date date
);
    DROP TABLE public.mt940_file;
       public         heap    postgres    false            �            1259    16738    mt940_file_mt940_id_seq    SEQUENCE     �   CREATE SEQUENCE public.mt940_file_mt940_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.mt940_file_mt940_id_seq;
       public          postgres    false    233            t           0    0    mt940_file_mt940_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.mt940_file_mt940_id_seq OWNED BY public.mt940_file.mt940_id;
          public          postgres    false    232            �            1259    16715    transaction    TABLE     �  CREATE TABLE public.transaction (
    transactionid integer NOT NULL,
    moduleid integer NOT NULL,
    bankid integer NOT NULL,
    customerid integer NOT NULL,
    date date NOT NULL,
    description character varying(255) NOT NULL,
    amount numeric(10,2) NOT NULL,
    currency character varying(10) NOT NULL,
    customer_info character varying(255) NOT NULL,
    bank_info character varying(255) NOT NULL,
    guess_entry_date date NOT NULL,
    transaction_detail character varying(255) NOT NULL,
    amount_available numeric(10,2) NOT NULL,
    status character varying(20) NOT NULL,
    forward_balance numeric(10,2) NOT NULL
);
    DROP TABLE public.transaction;
       public         heap    postgres    false            �            1259    16714    transaction_transactionid_seq    SEQUENCE     �   CREATE SEQUENCE public.transaction_transactionid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.transaction_transactionid_seq;
       public          postgres    false    231            u           0    0    transaction_transactionid_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.transaction_transactionid_seq OWNED BY public.transaction.transactionid;
          public          postgres    false    230            �            1259    16689    transaction_types    TABLE     �   CREATE TABLE public.transaction_types (
    transaction_type_id integer NOT NULL,
    transaction_type_name character varying(50) NOT NULL,
    category_id integer NOT NULL,
    bar_id integer NOT NULL
);
 %   DROP TABLE public.transaction_types;
       public         heap    postgres    false            �            1259    16688 )   transaction_types_transaction_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.transaction_types_transaction_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 @   DROP SEQUENCE public.transaction_types_transaction_type_id_seq;
       public          postgres    false    227            v           0    0 )   transaction_types_transaction_type_id_seq    SEQUENCE OWNED BY     w   ALTER SEQUENCE public.transaction_types_transaction_type_id_seq OWNED BY public.transaction_types.transaction_type_id;
          public          postgres    false    226            �           2604    16624    accounting_module moduleid    DEFAULT     �   ALTER TABLE ONLY public.accounting_module ALTER COLUMN moduleid SET DEFAULT nextval('public.accounting_module_moduleid_seq'::regclass);
 I   ALTER TABLE public.accounting_module ALTER COLUMN moduleid DROP DEFAULT;
       public          postgres    false    215    214    215            �           2604    16709    admin adminid    DEFAULT     n   ALTER TABLE ONLY public.admin ALTER COLUMN adminid SET DEFAULT nextval('public.admin_adminid_seq'::regclass);
 <   ALTER TABLE public.admin ALTER COLUMN adminid DROP DEFAULT;
       public          postgres    false    228    229    229            �           2604    16631    bank bankid    DEFAULT     j   ALTER TABLE ONLY public.bank ALTER COLUMN bankid SET DEFAULT nextval('public.bank_bankid_seq'::regclass);
 :   ALTER TABLE public.bank ALTER COLUMN bankid DROP DEFAULT;
       public          postgres    false    216    217    217            �           2604    16680 	   bar barid    DEFAULT     f   ALTER TABLE ONLY public.bar ALTER COLUMN barid SET DEFAULT nextval('public.bar_barid_seq'::regclass);
 8   ALTER TABLE public.bar ALTER COLUMN barid DROP DEFAULT;
       public          postgres    false    224    225    225            �           2604    16668    category categoryid    DEFAULT     z   ALTER TABLE ONLY public.category ALTER COLUMN categoryid SET DEFAULT nextval('public.category_categoryid_seq'::regclass);
 B   ALTER TABLE public.category ALTER COLUMN categoryid DROP DEFAULT;
       public          postgres    false    223    222    223            �           2604    16640    club clubid    DEFAULT     j   ALTER TABLE ONLY public.club ALTER COLUMN clubid SET DEFAULT nextval('public.club_clubid_seq'::regclass);
 :   ALTER TABLE public.club ALTER COLUMN clubid DROP DEFAULT;
       public          postgres    false    219    218    219            �           2604    16652    customer customer_id    DEFAULT     {   ALTER TABLE ONLY public.customer ALTER COLUMN customer_id SET DEFAULT nextval('public.customer_customerid_seq'::regclass);
 C   ALTER TABLE public.customer ALTER COLUMN customer_id DROP DEFAULT;
       public          postgres    false    221    220    221            �           2604    16742    mt940_file mt940_id    DEFAULT     z   ALTER TABLE ONLY public.mt940_file ALTER COLUMN mt940_id SET DEFAULT nextval('public.mt940_file_mt940_id_seq'::regclass);
 B   ALTER TABLE public.mt940_file ALTER COLUMN mt940_id DROP DEFAULT;
       public          postgres    false    233    232    233            �           2604    16718    transaction transactionid    DEFAULT     �   ALTER TABLE ONLY public.transaction ALTER COLUMN transactionid SET DEFAULT nextval('public.transaction_transactionid_seq'::regclass);
 H   ALTER TABLE public.transaction ALTER COLUMN transactionid DROP DEFAULT;
       public          postgres    false    231    230    231            �           2604    16692 %   transaction_types transaction_type_id    DEFAULT     �   ALTER TABLE ONLY public.transaction_types ALTER COLUMN transaction_type_id SET DEFAULT nextval('public.transaction_types_transaction_type_id_seq'::regclass);
 T   ALTER TABLE public.transaction_types ALTER COLUMN transaction_type_id DROP DEFAULT;
       public          postgres    false    226    227    227            T          0    16621    accounting_module 
   TABLE DATA           B   COPY public.accounting_module (moduleid, module_name) FROM stdin;
    public          postgres    false    215   |j       b          0    16706    admin 
   TABLE DATA           O   COPY public.admin (adminid, firstname, lastname, email, password_) FROM stdin;
    public          postgres    false    229   �j       V          0    16628    bank 
   TABLE DATA           ?   COPY public.bank (bankid, bank_name, banklocation) FROM stdin;
    public          postgres    false    217   �j       ^          0    16677    bar 
   TABLE DATA           8   COPY public.bar (barid, bar_name, moduleid) FROM stdin;
    public          postgres    false    225   �j       \          0    16665    category 
   TABLE DATA           G   COPY public.category (categoryid, category_name, moduleid) FROM stdin;
    public          postgres    false    223   k       X          0    16637    club 
   TABLE DATA           i   COPY public.club (clubid, clubname, club_address, club_city, club_phone, club_email, bankid) FROM stdin;
    public          postgres    false    219   6k       Z          0    16649    customer 
   TABLE DATA           �   COPY public.customer (customer_id, username, password_, first_name, last_name, email, phone_number, address, clubid) FROM stdin;
    public          postgres    false    221   �k       f          0    16739 
   mt940_file 
   TABLE DATA           �  COPY public.mt940_file (mt940_id, status, funds_code, amount, id, customer_reference, bank_reference, extra_details, currency, date, entry_date, guessed_entry_date, transaction_details, final_closing_balance, final_closing_balance_currency, final_closing_balance_date, available_balance, available_balance_currency, available_balance_date, forward_available_balance, forward_available_balance_currency, forward_available_balance_date) FROM stdin;
    public          postgres    false    233   ^n       d          0    16715    transaction 
   TABLE DATA           �   COPY public.transaction (transactionid, moduleid, bankid, customerid, date, description, amount, currency, customer_info, bank_info, guess_entry_date, transaction_detail, amount_available, status, forward_balance) FROM stdin;
    public          postgres    false    231   {n       `          0    16689    transaction_types 
   TABLE DATA           l   COPY public.transaction_types (transaction_type_id, transaction_type_name, category_id, bar_id) FROM stdin;
    public          postgres    false    227   �n       w           0    0    accounting_module_moduleid_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.accounting_module_moduleid_seq', 1, false);
          public          postgres    false    214            x           0    0    admin_adminid_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.admin_adminid_seq', 1, false);
          public          postgres    false    228            y           0    0    bank_bankid_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.bank_bankid_seq', 2, true);
          public          postgres    false    216            z           0    0    bar_barid_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.bar_barid_seq', 1, false);
          public          postgres    false    224            {           0    0    category_categoryid_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.category_categoryid_seq', 1, false);
          public          postgres    false    222            |           0    0    club_clubid_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.club_clubid_seq', 16, true);
          public          postgres    false    218            }           0    0    customer_customerid_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.customer_customerid_seq', 7, true);
          public          postgres    false    220            ~           0    0    mt940_file_mt940_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.mt940_file_mt940_id_seq', 1, false);
          public          postgres    false    232                       0    0    transaction_transactionid_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.transaction_transactionid_seq', 1, false);
          public          postgres    false    230            �           0    0 )   transaction_types_transaction_type_id_seq    SEQUENCE SET     X   SELECT pg_catalog.setval('public.transaction_types_transaction_type_id_seq', 1, false);
          public          postgres    false    226            �           2606    16626 (   accounting_module accounting_module_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.accounting_module
    ADD CONSTRAINT accounting_module_pkey PRIMARY KEY (moduleid);
 R   ALTER TABLE ONLY public.accounting_module DROP CONSTRAINT accounting_module_pkey;
       public            postgres    false    215            �           2606    16713    admin admin_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (adminid);
 :   ALTER TABLE ONLY public.admin DROP CONSTRAINT admin_pkey;
       public            postgres    false    229            �           2606    16635    bank bank_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.bank
    ADD CONSTRAINT bank_pkey PRIMARY KEY (bankid);
 8   ALTER TABLE ONLY public.bank DROP CONSTRAINT bank_pkey;
       public            postgres    false    217            �           2606    16682    bar bar_pkey 
   CONSTRAINT     M   ALTER TABLE ONLY public.bar
    ADD CONSTRAINT bar_pkey PRIMARY KEY (barid);
 6   ALTER TABLE ONLY public.bar DROP CONSTRAINT bar_pkey;
       public            postgres    false    225            �           2606    16670    category category_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (categoryid);
 @   ALTER TABLE ONLY public.category DROP CONSTRAINT category_pkey;
       public            postgres    false    223            �           2606    16642    club club_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.club
    ADD CONSTRAINT club_pkey PRIMARY KEY (clubid);
 8   ALTER TABLE ONLY public.club DROP CONSTRAINT club_pkey;
       public            postgres    false    219            �           2606    16656    customer customer_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (customer_id);
 @   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_pkey;
       public            postgres    false    221            �           2606    16658    customer customer_username_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_username_key UNIQUE (username);
 H   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_username_key;
       public            postgres    false    221            �           2606    16746    mt940_file mt940_file_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.mt940_file
    ADD CONSTRAINT mt940_file_pkey PRIMARY KEY (mt940_id);
 D   ALTER TABLE ONLY public.mt940_file DROP CONSTRAINT mt940_file_pkey;
       public            postgres    false    233            �           2606    16722    transaction transaction_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.transaction
    ADD CONSTRAINT transaction_pkey PRIMARY KEY (transactionid);
 F   ALTER TABLE ONLY public.transaction DROP CONSTRAINT transaction_pkey;
       public            postgres    false    231            �           2606    16694 (   transaction_types transaction_types_pkey 
   CONSTRAINT     w   ALTER TABLE ONLY public.transaction_types
    ADD CONSTRAINT transaction_types_pkey PRIMARY KEY (transaction_type_id);
 R   ALTER TABLE ONLY public.transaction_types DROP CONSTRAINT transaction_types_pkey;
       public            postgres    false    227            �           2606    16683    bar bar_moduleid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.bar
    ADD CONSTRAINT bar_moduleid_fkey FOREIGN KEY (moduleid) REFERENCES public.accounting_module(moduleid);
 ?   ALTER TABLE ONLY public.bar DROP CONSTRAINT bar_moduleid_fkey;
       public          postgres    false    215    225    3495            �           2606    16671    category category_moduleid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_moduleid_fkey FOREIGN KEY (moduleid) REFERENCES public.accounting_module(moduleid);
 I   ALTER TABLE ONLY public.category DROP CONSTRAINT category_moduleid_fkey;
       public          postgres    false    223    215    3495            �           2606    16643    club club_bankid_fkey    FK CONSTRAINT     v   ALTER TABLE ONLY public.club
    ADD CONSTRAINT club_bankid_fkey FOREIGN KEY (bankid) REFERENCES public.bank(bankid);
 ?   ALTER TABLE ONLY public.club DROP CONSTRAINT club_bankid_fkey;
       public          postgres    false    3497    219    217            �           2606    16659    customer customer_clubid_fkey    FK CONSTRAINT     ~   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_clubid_fkey FOREIGN KEY (clubid) REFERENCES public.club(clubid);
 G   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_clubid_fkey;
       public          postgres    false    3499    219    221            �           2606    16728 #   transaction transaction_bankid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaction
    ADD CONSTRAINT transaction_bankid_fkey FOREIGN KEY (bankid) REFERENCES public.bank(bankid);
 M   ALTER TABLE ONLY public.transaction DROP CONSTRAINT transaction_bankid_fkey;
       public          postgres    false    231    3497    217            �           2606    16733 '   transaction transaction_customerid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaction
    ADD CONSTRAINT transaction_customerid_fkey FOREIGN KEY (customerid) REFERENCES public.customer(customer_id);
 Q   ALTER TABLE ONLY public.transaction DROP CONSTRAINT transaction_customerid_fkey;
       public          postgres    false    231    221    3501            �           2606    16723 %   transaction transaction_moduleid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaction
    ADD CONSTRAINT transaction_moduleid_fkey FOREIGN KEY (moduleid) REFERENCES public.accounting_module(moduleid);
 O   ALTER TABLE ONLY public.transaction DROP CONSTRAINT transaction_moduleid_fkey;
       public          postgres    false    3495    215    231            �           2606    16700 /   transaction_types transaction_types_bar_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaction_types
    ADD CONSTRAINT transaction_types_bar_id_fkey FOREIGN KEY (bar_id) REFERENCES public.bar(barid);
 Y   ALTER TABLE ONLY public.transaction_types DROP CONSTRAINT transaction_types_bar_id_fkey;
       public          postgres    false    225    227    3507            �           2606    16695 4   transaction_types transaction_types_category_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaction_types
    ADD CONSTRAINT transaction_types_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.category(categoryid);
 ^   ALTER TABLE ONLY public.transaction_types DROP CONSTRAINT transaction_types_category_id_fkey;
       public          postgres    false    223    227    3505            T      x������ � �      b      x������ � �      V   6   x�3�JL�WpJ���t�-.I-JI��2���sWp*�t��K��/K������ F�X      ^      x������ � �      \      x������ � �      X   z   x�5˱
�0����)|�`�4�V]����iN=h���o�Zp���õD�n΢З�:R��b8I������[�����=EͲ[������TG��T��Hi��������:�7�(	�"�U)      Z   �  x�U��n9�����!Q�(�%(��I��n�6���$�����j�6ا_�c�f�F ��#�7������Ⓞ͏�������֗�C
5K1�<�h��A�Ĝb�	M�Ȕ�L��R��(U�>��O=�>�Y�ݨ��)8<���[��ew�ٚ[�^eY}�_�V�ǅu}pF��58�*Yrq�j4.��}����X�G�Y��٤�������v�x3).�=?��? �Gr��5SY����H��W��v�'���EGY��v):,� �΀vњH����"��/�&��):�(���\��g��ـAq�Z�� ]���������n���_W�������b��k�I\(�ݹBko�����^#�m��%�ר6�b>�����T�S�q�bV��bǗ>�F���"�� �S�S	�}��MT{�\r�,S�l|��^���}ԅK>��G�������>��6���u�g�|�	�xuW�A޾��x���Br?�wt.��=�6��D�{t�K=c�}ɾ��Z�ϫ�2�����p�����v"��?n��v������0Y�$B�}����#�ɀ�� t�rI� �<_=m�kջ�i��g�xZ-�-����B�uD��F��C6�m��}yvv�7�G%�      f      x������ � �      d      x������ � �      `      x������ � �     