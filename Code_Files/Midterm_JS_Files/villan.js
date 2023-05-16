const topVillains = [
    { name: "Venom", image: "https://i.imgur.com/fwnk2J1.jpeg" },
    { name: "neat", image: "https://i.imgur.com/bwGZ31S.jpg" },
    { name: "Joker", image: "https://i.imgur.com/1fnzDRf.jpg" },
  ];
  
  const fourthVillain = {
    name: "Freddy Krueger",
    image: "https://i.imgur.com/fwnk2J1.jpeg",
  };
  
  let userInput = '';
  
  while (userInput !== 'quit' && userInput !== 'exit') {
    userInput = prompt("Who is your favorite movie villain?");
  
    let villain = topVillains.find((v) => v.name.toLowerCase() === userInput.toLowerCase());
  
    if (villain) {
      alert(`Here's an image of ${villain.name}:`);
      const img = document.createElement("img");
      img.src = villain.image;
      document.body.appendChild(img);
    } else {
      alert(`Sorry, ${userInput} is not one of my top 3 favorite villains. Here's an image of ${fourthVillain.name}:`);
      const img = document.createElement("img");
      img.src = fourthVillain.image;
      document.body.appendChild(img);
    }
  } 