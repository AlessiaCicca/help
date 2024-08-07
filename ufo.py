
//stato
from dataclasses import dataclass

@dataclass
class Stato:
    id:str
    Name:str
    Capital:str
    Lat:float
    Lng:float
    Area:int
    Population:int
    Neighbors:str


    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.Name}"


//avvistamenti 
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Sighting:
    id: int
    7: datetime
    city: str
    state: str
    country:str
    shape: str
    duration: int
    duration_hm: str
    comments: str
    date_posted: datetime
    latitude: float
    longitude: float


    def __str__(self):
        return self.country

    def __hash__(self):
        return hash(self.id)
        
        
//I vertici del grafo saranno gli stati americani (o meglio, il sottoinsieme di stati
in cui vi è stato almeno un avvistamento nell'anno)

        select distinct s.state as stato
        from sighting s 
        where s.country ='us' and year(s.`datetime`) =%s
        group by s.state 
        having count(s.id)>0

//Gli archi del grafo rappresentano l'ordine temporale degli avvistamenti.
In particolare, ci dovrà essere un arco tra lo stato A e lo stato B se almeno un
avvistamento in B è temporalmente successivo ad almeno un avvistamento in A
(sempre nell'anno di riferimento).

         select count(*) as peso
        from (select s.`datetime` as d1
        from sighting s 
        where s.country ='us' and s.state =%s
        and year(s.`datetime`)=%s) as t1,
        (select s.`datetime` as d2
        from sighting s 
        where s.country ='us' and s.state =%s
        and year(s.`datetime`)=%s) as t2
        where d1<d2

//Facendo click sul bottone CREA GRAFO, creare un grafo semplice, pesato e non orientato, i cui vertici siano
tutti gli stati presenti nella tabella “state”. Un arco collega due stati solo se sono confinanti, come indicato
nella tabella “neighbor”.

        select distinct *
         from state s

        select distinct n.state1 as v1, n.state2 as v2
        from neighbor n 
        where n.state1<n.state2

//Il peso dell’arco viene calcolato come il numero di avvistamenti che hanno la stessa forma (colonna “shape”)
selezionata dal menù a tendina Forma, e che si sono verificati nello stesso anno selezionato (da estrarre dalla
colonna “datetime”), nei due stati considerati.

        select count(*) as peso
        from sighting s 
        where s.shape=%s and year(s.`datetime`)=%s and (s.state=%s or s.state=%s)



public List<StringPair> getEdges(Year anno) {
		String sql = "select s1.state as state1 , s2.state as state2, count(*) " + 
				"from sighting s1, sighting s2 " + 
				"where year(s1.datetime)=year(s2.datetime) " + 
				"and year(s1.datetime)=? " + 
				"and s1.country='us' " + 
				"and s2.country='us' " + 
				"and s2.datetime>s1.datetime " + 
				"and s1.state<>s2.state " + 
				"group by s1.state, s2.state " ;
		
		try {
			Connection conn = DBConnect.getConnection() ;
			PreparedStatement st = conn.prepareStatement(sql) ;
			
			st.setInt(1, anno.getValue());
			
			ResultSet res = st.executeQuery() ;
			
			List<StringPair>list = new ArrayList<>() ;
			while(res.next()) {
				list.add(new StringPair(res.getString("state1"), res.getString("state2"))) ;
			}
			conn.close();
			return list ;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return null ;
		}
		
	}
//CON FORMA E ANNO DATI
select t1.a1,t2.a2, t1.d1, t2.d2
from (select s.id as a1, s.state as s1, s.`datetime` as d1
from sighting s 
where s.shape ='oval' and year(s.`datetime`)=2002) as t1,
(select s.id as a2, s.state as s2,  s.`datetime` as d2
from sighting s 
where s.shape ='oval' and year(s.`datetime`)=2002) as t2
where t1.s1=t2.s2 and t1.a1<t2.a2


//CON FORMA E ANNO NON DATI
select t1.a1,t2.a2, t1.d1, t2.d2
from (select s.id as a1, s.state as s1, s.`datetime` as d1,
s.shape as f1
from sighting s ) as t1,
(select s.id as a2, s.state as s2,  s.`datetime` as d2, s.shape as f2
from sighting s 
where s.shape ='oval' and year(s.`datetime`)=2002) as t2
where t1.s1=t2.s2 and t1.a1<t2.a2
and t1.f1=t2.f2 and year(t1.d1)= year(t2.d2)


//CON FORMA E ANNO

    def addEdges(self, forma,anno):
        self.grafo.clear_edges()
        allEdges = DAO.getConnessioni(forma,anno)
        for connessione in allEdges:
            nodo1 = self._idMap[connessione.v1]
            nodo2 = self._idMap[connessione.v2]
            if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                if self.grafo.has_edge(nodo1, nodo2) == False:
			if connessione.d1<connessione.d2:
                   		 self.grafo.add_edge(nodo1, nodo2, weight=peso)
			if connessione.d2<connessione.d1:
				self.grafo.add_edge(nodo1, nodo1, weight=peso)

//SENZA FORMA E ANNO

    def addEdges(self):
        self.grafo.clear_edges()
        allEdges = DAO.getConnessioni()
        for connessione in allEdges:
            nodo1 = self._idMap[connessione.v1]
            nodo2 = self._idMap[connessione.v2]
            if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                if self.grafo.has_edge(nodo1, nodo2) == False:
			if connessione.d1<connessione.d2:
                   		 self.grafo.add_edge(nodo1, nodo2, weight=peso)
			if connessione.d2<connessione.d1:
				self.grafo.add_edge(nodo1, nodo1, weight=peso)


//RIEMPIMENTO FORME IN BASE AD ANNO
//VIEW
	
 self.dd_anno=ft.Dropdown(label="Anno", on_change=self._controller.fillDDforme)
self.dd_shape=ft.Dropdown(label="Shape")
self._controller.fillDDanno()

//CONTROLLER
    def fillDDanno(self):
            anni=self._model.getAnni
            for anno in anni:
                self._view.dd_anno.options.append(ft.dropdown.Option(
                    text=anno))

    def fillDDforme(self,e):
        self._view.dd_shape.options=[]
        forme=self._model.getForme(int(self._view.dd_anno.value))
        for forma in forme:
            self._view.dd_shape.options.append(ft.dropdown.Option(
                text=forma))
        self._view.update_page()

