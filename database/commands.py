#SQL queries

create_tables = (
    """
    CREATE TABLE IF NOT EXISTS info (
        Region CHAR(100) NOT NULL,
        Exchange  CHAR(100) NOT NULL,
        Index  CHAR(20) NOT NULL,
        Currency  CHAR(15) NOT NULL;
    )
    """,

    """ CREATE TABLE IF NOT EXISTS data (
            Key INT,
            Index CHAR(20) ,
            Date DATE ,
            Open CHAR(50) ,
            High  CHAR(50) ,
            Low CHAR(50) ,
            Close CHAR(50) ,
            Adj_Close CHAR(50) ,
            Volume CHAR(50) ;
            )
    """,
    """
    CREATE TABLE IF NOT EXISTS  processed (
            Key INT,
            Index CHAR(20) NOT NULL,
            Date DATE NOT NULL,
            Open  DOUBLE PRECISION NOT NULL,
            High  DOUBLE PRECISION NOT NULL,
            Low  DOUBLE PRECISION NOT NULL,
            Close  DOUBLE PRECISION NOT NULL,
            Adj_Close  DOUBLE PRECISION NOT NULL,
            Volume  DOUBLE PRECISION NOT NULL,
            CloseUSD DOUBLE PRECISION;

    )
    """)


create_views = (
        """
        CREATE OR REPLACE VIEW V_PROCESSED AS
        select * from
        (select min(low) as min_low ,max(open) as max_open,
                    CAST(extract(YEAR from date) as varchar(4)) as year,
                    CAST(extract(MONTH from date) as varchar(2))as month,
                    index as ind
                    from processed
                    group by year,month,ind) as t
                    join info on index = t.ind
                    order by region asc;
        """,
        #### Korea region is not processed
        """ CREATE OR REPLACE VIEW V_NOTPROCESSED AS 
            select distinct key,date,open,high,low,
            close,adj_close,volume,region,
            exchange,currency  from (select * from (SELECT d.* FROM data d
            WHERE NOT EXISTS ( SELECT 1 FROM
            processed p WHERE d.index = p.index) )as a
            left JOIN  info i on a.index = i.index) as al;
        """,
### остальные создовал для себя как дополнительно что то сделать
        """ 
            create or replace view v_processed_second
            select * from
            (select min(low) as min_low ,sum(volume) as sum_volume,max(high) as max_high,
                        CAST(extract(YEAR from date) as varchar(4)) as year,
                          CAST(extract(MONTH from date) as varchar(2))as month,
                          index as ind
                          from processed
                          group by year,month,ind) as t
                          join info on index = t.ind
                          order by region asc;
        
              """,

            """ create or replace view v_processed_with_day as 
                select * from(select processed.index as ind,date,open,high,low,
                close,adj_close,volume,region,
                exchange,currency from  processed
                join info on info.index=processed.index
                order by region) as t;
            """
     )


get_view_processed = ("""
    select * from v_processed
    order by region asc;
""")

get_view_processed_second = ("""
    select * from v_processed_second
    order by region asc;
""")

get_view_processed_with_day = ("""
    select * from v_processed_with_day
    order by region asc;
""")