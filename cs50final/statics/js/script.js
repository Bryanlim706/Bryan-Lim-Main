document.addEventListener("DOMContentLoaded", function() {
    const deleteButtons = document.querySelectorAll('.delete-btn');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const categoryItem = event.target.closest('.nav-item');
            categoryItem.remove(); // Remove the list item (category)
            // Optionally, you can send an AJAX request to update the backend (e.g., to delete from the database)
        });
    });
});