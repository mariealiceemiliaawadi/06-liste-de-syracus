#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """
    Retourne la suite de Syracuse de source n sous forme de liste.
    """
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    # votre code ici
    l = [n]
    while n != 1: #tant que n différent de 1
        if n % 2 == 0: #n pair
            n = n//2 
        else:           # n impair
            n = 3*n+1
        l.append(n)  # on ajoute le nouveau n à la fin de la liste
    return l
    

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
   
    """
    Le temps de vol = nombre d'itérations nécessaires
    pour atteindre 1 (longueur de la liste - 1).
    """
    # votre code ici

    temps_de_vol = len(l)-1
    return temps_de_vol

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici
    i = 1
    ref = l[0]
    # print(i, len(l), ref)

    while i < len(l) and l[i] > ref :
        # print(i, l[i], ref)
        i += 1
    return i-1


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    
    # votre code ici
    
    return max(l)


#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    lsyr = syracuse_l(15) # suite de Syracuse avec n=15
    # syr_plot(lsyr) # affichage graphique
    # print(temps_de_vol(lsyr))  # affichage du temps de vol
    print(temps_de_vol_en_altitude(lsyr))  # affichage du temps de vol en altitude
    # print(altitude_maximale(lsyr))  # affichage de l'altitude maximale


if __name__ == "__main__":
    main()