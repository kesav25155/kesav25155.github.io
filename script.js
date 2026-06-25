/**
 * Tab Navigation System
 * Handles tab switching between About, Projects, Contacts, and Perficient
 */

document.addEventListener('DOMContentLoaded', function() {
  const navLinks = document.querySelectorAll('.nav-link');
  const tabContents = document.querySelectorAll('.tab-content');

  // Click handler for nav links
  navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();

      const tabName = this.getAttribute('data-tab');
      const tabElement = document.getElementById(tabName + '-tab');

      if (!tabElement) return;

      // Remove active class from all
      navLinks.forEach(l => l.classList.remove('active'));
      tabContents.forEach(t => t.classList.remove('active'));

      // Add active class to current
      this.classList.add('active');
      tabElement.classList.add('active');

      // Scroll to top smoothly
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  });

  // Set initial active state
  const firstLink = navLinks[0];
  if (firstLink) {
    firstLink.classList.add('active');
  }
});

