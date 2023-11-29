import {
  Box,
  ImageList,
  ImageListItem,
  ImageListItemBar,
  Typography,
} from "@mui/material";

interface IMenuPlatillo {
  cambiarMenu: (opcion: number) => void;
  selectPlatillo: (platillo: string) => void;
}
const MenuPlatillo: React.FC<IMenuPlatillo> = ({
  selectPlatillo,
}) => {
  const platillos = [
    {
      img: "https://www.clarin.com/img/2022/03/07/0w2kcAVNO_1256x620__1.jpg",
      nombre: "Asado",
    },
    {
      img: "https://images.pexels.com/photos/1251198/pexels-photo-1251198.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
      nombre: "Hamburguesa",
    },
    {
      img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8UzxYcdhEKQYKnRU76u88SoqLOXUEiIjarIjDs7j1ObOjQmlFuEks82WAR8KMlytXRV8&usqp=CAU",
      nombre: "Brochetas",
    },
    {
      img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs8-mGflQuQN9oiMgaTzCSEh6rkpnLcgu3XPpf3qTY3mc1WYkAwFBggirvWH5iOkrluGs&usqp=CAU",
      nombre: "Churrasco",
    },
    {
      img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeiWP1fpYfZ-MOvi0h7BLz1t5LF8Ury_ZWT77ElGeawnozG9nI3pcKBIBa_7qTARN5AfU&usqp=CAU",
      nombre: "Milanesa",
    },
    {
      img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1rwXxvMZSyFKTxeYEeqqzoB54vNRfFkKQThvvbI8A9S7gaZUXbLuheMtsf1YE7J2OxoI&usqp=CAU",
      nombre: "Lampreado",
    },
    {
      img: "https://assets.unileversolutions.com/recipes-v2/239857.jpg?im=Resize,height=530;Crop,size=(540,530),gravity=Center",
      nombre: "Empanadas",
    },
    {
      img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEP9Z9uQsTQmiIcIWsoXWJI7JLM9AS_y_Y0dKu4jD_XImb3azEVkIBiy3BEI9zOHRaACE&usqp=CAU",
      nombre: "Albóndigas",
    },
    {
      img: "https://mandolina.co/wp-content/uploads/2023/07/estofado-de-res.png",
      nombre: "Estofado",
    },
    {
      img: "https://www.recetasnestlecam.com/sites/default/files/styles/recipe_detail_desktop/public/srh_recipes/3862d7635d44c8f9834ff46ac64b53ae.webp?itok=PFpaTscx",
      nombre: "Sopa",
    },
    {
      img: "https://www.paulinacocina.net/wp-content/uploads/2021/09/goulash-noodles-eat-food-thumbnail-1.jpg",
      nombre: "Guiso",
    },
    {
      img: "https://canalcocina.es/medias/publicuploads/2013/02/07/105958/09mpmpr9sy17imzhtpit.jpg",
      nombre: "Locro",
    },
    {
      img: "https://www.cronica.com.ar/__export/1668270130239/sites/cronica/img/2022/11/12/carne_a_la_olla_crop1668268344208.jpg_2001513285.jpg",
      nombre: "Carne a la olla",
    },
    {
      img: "https://media.lacapital.com.ar/p/a8535113ee273a29b3a46f4225b35df3/adjuntos/205/imagenes/018/078/0018078012/1200x675/smart/pastel-carne1jpg.jpg",
      nombre: "Pastel de papa",
    },
    {
      img: "https://i.blogs.es/af32e6/matambre_relleno/1366_2000.jpeg",
      nombre: "Arrolado de carne",
    },
    {
      img: "https://assets.unileversolutions.com/recipes-v2/231480.jpg",
      nombre: "Pan de carne",
    },
    {
      img: "https://pastaslamuneca.com/wp-content/uploads/2021/05/lasana-en-salsa-bechamel.jpg",
      nombre: "Lasaña",
    },
    {
      img: "https://imag.bonviveur.com/canelones-de-carne.jpg",
      nombre: "Canelones de carne",
    },
    {
      img: "https://3.bp.blogspot.com/_x6tWi2Yd_eM/S897mpwXFII/AAAAAAAAAa4/auXO8kkLlQE/s1600/johann_almoco_bife.jpg",
      nombre: "Bife",
    },
    {
      img: "https://cloudfront-us-east-1.images.arcpublishing.com/radiomitre/M6KFB4CSIBGR7C5JZRUFKBEYOE.jpg",
      nombre: "Carne a la plancha",
    },
  ];
  return (
    <Box>
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Typography
          component="h2"
          variant="h4"
          sx={{ mt: 2, color: "gray", fontWeight: "bold" }}
        >
          Selecciona el platillo que vas a preparar
        </Typography>
      </Box>
      <Box sx={{overflow:"auto"}}>
      <ImageList gap={9} sx={{ height: "600"}}>
          {platillos.map((item) => (
            <ImageListItem
                
              key={item.img}
              sx={{ cursor: "pointer",px:8 }}
              onClick={() => selectPlatillo(item.nombre)}
            >
              <img
                srcSet={`${item.img}?w=248&fit=crop&auto=format&dpr=2 2x`}
                src={`${item.img}?w=248&fit=crop&auto=format`}
                alt={item.nombre}
                loading="lazy"
              />
              <ImageListItemBar sx={{textAlign:"center",fontSize:30}} title={
                  <Typography variant="h5">
                  {item.nombre} 
                  </Typography>
              } position="below" />
            </ImageListItem>
          ))}
        </ImageList>
      </Box>
    </Box>
  );
};

export default MenuPlatillo;
