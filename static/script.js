// Function to fade out an element
function fadeOut(element) {
    element.classList.add('fade-out');
    setTimeout(() => {
        element.style.display = 'none';
    }, 500);
}

// Function to fade in an element
function fadeIn(element) {
    element.style.display = 'block';
    setTimeout(() => {
        element.classList.remove('fade-out');
        element.classList.add('fade-in');
    }, 10);
}

// Load Users
function loadUsers() {
    const userTable = document.querySelector('#userTable tbody');
    userTable.innerHTML = '<tr><td colspan="5">Loading...</td></tr>';

    fetch('/api/users')
        .then(response => response.json())
        .then(data => {
            userTable.innerHTML = '';
            data.forEach(user => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${user.id}</td>
                    <td>${user.name}</td>
                    <td>${user.email}</td>
                    <td>${user.mobile}</td>
                    <td><button class="delete-btn" onclick="confirmDeleteUser(${user.id})">Delete</button></td>
                `;
                userTable.appendChild(row);
            });
        });
}

// Add User
document.getElementById('userForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/api/add_user', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || data.error);
        loadUsers();
    });
});

// Confirm delete user
function confirmDeleteUser(userId) {
    if (confirm("Are you sure you want to delete this user?")) {
        deleteUser(userId);
    }
}

// Delete User
function deleteUser(userId) {
    fetch(`/api/delete_user/${userId}`, { method: 'DELETE' })
        .then(response => response.json())
        .then(data => {
            alert(data.message || data.error);
            loadUsers();
        });
}

// Load Expenses
function loadExpenses() {
    const expenseTable = document.querySelector('#expenseTable tbody');
    expenseTable.innerHTML = '<tr><td colspan="6">Loading...</td></tr>';

    fetch('/api/expenses')
        .then(response => response.json())
        .then(data => {
            expenseTable.innerHTML = '';
            data.forEach(expense => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${expense.id}</td>
                    <td>${expense.description}</td>
                    <td>${expense.amount}</td>
                    <td>${expense.split_method}</td>
                    <td>${JSON.stringify(expense.details)}</td>
                    <td><button class="delete-btn" onclick="confirmDeleteExpense(${expense.id})">Delete</button></td>
                `;
                expenseTable.appendChild(row);
            });
        });
}

// Add Expense
document.getElementById('expenseForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/api/add_expense', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || data.error);
        loadExpenses();
    });
});

// Confirm delete expense
function confirmDeleteExpense(expenseId) {
    if (confirm("Are you sure you want to delete this expense?")) {
        deleteExpense(expenseId);
    }
}

// Delete Expense
function deleteExpense(expenseId) {
    fetch(`/api/delete_expense/${expenseId}`, { method: 'DELETE' })
        .then(response => response.json())
        .then(data => {
            alert(data.message || data.error);
            loadExpenses();
        });
}

// Initial Load with Fade-in
document.addEventListener('DOMContentLoaded', () => {
    fadeIn(document.body);
    loadUsers();
    loadExpenses();
});
