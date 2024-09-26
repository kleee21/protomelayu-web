// Wait until the page is fully loaded
window.addEventListener('load', function() {
    // Keep the loading screen visible for at least 2 seconds
    setTimeout(function() {
      // Hide the loading screen
      const loadingScreen = document.getElementById('loading-screen');
      loadingScreen.style.display = 'none';
  
      // Add the 'loaded' class to body to show the content
      document.body.classList.add('loaded');
    }, 1000); // 2 seconds
  });