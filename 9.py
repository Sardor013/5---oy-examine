async function getUsers() {
  try {
    const response = await fetch('https://dummyjson.com/users');
    const data = await response.json();
    console.log(data); // Yoki, ma'lumotlarni istalgan shaklda ekranga chiqaring
    return data;
  } catch (error) {
    console.error('Xatolik yuz berdi:', error);
    throw error;
  }
}

// getUsers funksiyasini chaqirish
getUsers()
  .then(data => {
    // Ma'lumotlar bilan ishlash
  })
  .catch(error => {
    // Xatolikni boshqarish
  });
